from db import weightData, weightPopularityData
from models.weightModel import WeightData
from datetime import datetime

def createWeightData(user:str):
    newWeightData ={
        'user':user,
        'family':{'totals':0,'daily':[0],'withinDay':[[0]]},
        'health':{'totals':0,'daily':[0],'withinDay':[[0]]},
        'work or school':{'totals':0,'daily':[0],'withinDay':[[0]]},
        'relationships':{'totals':0,'daily':[0],'withinDay':[[0]]},
        'spirituality or faith':{'totals':0,'daily':[0],'withinDay':[[0]]},        
        'days':[datetime.today()]
    }
    weightData.insert_one(newWeightData)
    for key in newWeightData.keys():
        if key!='user' and key!='days':
            updateWeightPopularity(key)
    return True

# increment the count of users with a given weight button by 1 when assigning user default weight buttons
def updateWeightPopularity(name:str):
    weightPopularityData.update_one(
        {'name':name},
        {
            '$inc':
            {
                'value':1
            }
        }
    )
    return True

def updateWeightData(user:str,newData:WeightData):
    index=len(weightData.find_one({'user':user})['days'])-1
    weightData.update_one({'user':user},
        { 
            '$inc':
                {newData.name+'.totals':newData.delta},    
             '$push':
                {newData.name+'.withinDay.'+str(index):newData.value},
             '$set':
                {newData.name+'.daily.'+str(index):newData.value}
        },
    )
    return True

def retrieveWeightData(user:str):
    if weightData.find({'user':user}).limit(1).count()<1:
        createWeightData(user=user)
    currentButtonValues=weightData.find_one({'user':user},{'_id': 0,'user':0})
    if currentButtonValues['days'][-1].day != datetime.today().day:
        return createNewDay(user=user,buttonNames=currentButtonValues.keys())
    else:
        buttons={}
        for key,value in currentButtonValues.items():
            if key != 'days':
                buttons[key]=value['withinDay'][-1][-1]
        return buttons

def createNewDay(user:str,buttonNames:list):
    newDayNewButtons={}
    for name in buttonNames:
        if name!='days':
            newDayNewButtons[name]=0
            weightData.update_one({'user':user},
                {
                    '$push':
                        {
                            name+'.withinDay':[0],
                            name+'.daily':0
                        }
                }
            )
        else:
            weightData.update_one({'user':user},
                {
                    '$push':
                        {
                            'days':datetime.today()
                        },
                }
            )
    return newDayNewButtons

def createNewButton(name:str,user:str):
    weightData.update_one({'user':user},
        { 
        '$set':
        {
        name+'.totals':0,
        name+'.daily':[0],
        name+'.withinDay':[[0]]
        }
    },
    ),
    if weightPopularityData.find({'name':name}).limit(1).count()<1:
        weightPopularityData.insert_one({'name':name,'value':1,'custom':True})
    else:
        weightPopularityData.update_one(
            {'name':name},
            {
                '$inc':
                {
                    'value':1
                }
            }
        )
    return True

def wipeButt(name:str,user:str):
    weightData.update_one(
        {'user':user},
        { '$unset': {name:""}}
    )
    weightPopularityData.update_one(
        {'name':name},
        {
            '$inc':
            {
                'value':-1
            }
        }
    )
    return True

def getPopularWeights():
    return weightPopularityData.aggregate(
    [
     { '$sort' : { 'name' : 1 } }
    ]
    )