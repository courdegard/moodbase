from db import weightData, weightPopularityData
from models.weightModel import WeightData
from modules.HelperFunctions import returnDay


def createWeightConfigDocument(user: str):
    defaultWeightConfig = {
        'user': f"{user}!weightconfig",
        'family': {'dateAdded': returnDay(), 'valueToDate': 0},
        'health': {'dateAdded': returnDay(), 'valueToDate': 0},
        'work': {'dateAdded': returnDay(), 'valueToDate': 0},
        'school': {'dateAdded': returnDay(), 'valueToDate': 0},
        'relationships': {'dateAdded': returnDay(), 'valueToDate': 0},
        'spirituality,faith': {'dateAdded': returnDay(), 'valueToDate': 0}
    }
    weightData.insert_one(defaultWeightConfig)
    for key in defaultWeightConfig.keys():
        if key != 'user':
            updateWeightPopularity(key)
    return defaultWeightConfig

# increment the count of users with a given weight button by 1 when assigning user default weight buttons


def updateWeightPopularity(name: str):
    weightPopularityData.update_one(
        {'name': name},
        {
            '$inc':
            {
                'value': 1
            }
        },
        upsert=True
    )
    return True


def updateWeightData(user: str, newData: WeightData):
    weightData.update_one(
        {'user': user},
        {
            '$inc':
                {newData.name+'.'+newData.timerange: newData.delta},
        },
        upsert=True
    )
    return True


def retrieveWeightData(user: str):
    if weightData.find({'user': f"{user}!weightconfig"}).limit(1).count() < 1:
        return createWeightConfigDocument(user)
    else:
        weightConfig = weightData.find_one({'user': f"{user}!weightconfig"}, {'_id': 0, 'user': 0})
        if weightData.find({'user': f"{user}!{returnDay()}"}).limit(1).count() > 0:
            return {
                'config': weightConfig,
                'todaysData': weightData.find_one({'user': f"{user}!{returnDay()}"}, {'_id': 0, 'user': 0})
            }  
        else:
            return {
                'config': weightConfig,
                'todaysData': False
            }

def createNewButton(name: str, user: str):
    weightData.update_one({'user': f"{user}!weightconfig"},
                          {
            '$set':
            {
                name: 0
            }
        },
    ),
    updateWeightPopularity(name)
    return True


def wipeButt(name: str, user: str):
    weightData.update_one(
        {'user': f"{user}!weightconfig"},
        {'$unset': {name: ""}}
    )
    weightPopularityData.update_one(
        {'name': name},
        {
            '$inc':
            {
                'value': -1
            }
        }
    )
    return True


def getPopularWeights():
    return weightPopularityData.aggregate(
        [
            {'$sort': {'name': 1}}
        ]
    )
