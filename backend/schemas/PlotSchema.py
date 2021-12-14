from db import plotData
from datetime import date, timedelta
from models.plotModel import PlotDataSubmission
from modules.HelperFunctions import returnDay, getYesterday
# from bson import Decimal128


def createPlotDataDocument(user: str, newData: PlotDataSubmission):
    plotData.insert_one(
        {
            'user': user,
            'day': returnDay()
        }
    )
    return True

def updateUserPlotDataDocument(user: str, newData: PlotDataSubmission):
    plotData.update_one(
        {
            'user': user,
            'day': returnDay()
        },
        {
        '$set':
            {
                newData.timerange: createDataDict(newData),
            },
        },
        upsert = True
    )
    return True


def createDataDict(data: PlotDataSubmission):
    return {
        'happiness': data.happiness,
        'calm': data.calm,
        'mapX': data.mapX,
        'mapY': data.mapY
    }


def updateMean(n: int, old: float, new: float, modifier: int):
    return ((float(str(old))*n)+float(str(new)))/(n+modifier)


def updateDailyCommunityData(newData: PlotDataSubmission):
    if plotData.find({'user': "!community", 'day': returnDay()}).limit(1).count() < 1:
        plotData.insert_one(
            {
                'user': "!community",
                'day': returnDay(),
                newData.timerange: createDataDict(newData),
                'clickCount': 1
            }
        )
        setNewMeansAllTime()
        return True
    currentCommunityValues = plotData.find_one(
        {'user': "!community", 'day':returnDay()})
    if newData.timerange in currentCommunityValues:
        plotData.update_one(
            {
                'user': "!community",
                'day': returnDay()
            },
            {
                '$set':
                {
                    newData.timerange: setNewMeansDaily(
                        currentCommunityValues, newData)
                },
                '$inc':
                {
                    'clickCount': 1
                }
             },
             upsert=True
        )
    else:
        updateUserPlotDataDocument("!community", newData)
    return

def setNewMeansAllTime():
    if plotData.find({'user': "!community", 'day':getYesterday(returnDay())}).limit(1).count()<1:
        return
    yesterdaysNews = plotData.find_one(
        {'user': "!community", 'day':getYesterday(returnDay())})
    allTime = plotData.find_one({'user': '!communityAllTime'})
    timeRangeLoop = ['morning', 'midday', 'evening']
    variableKeyLoop = ['happiness', 'calm', 'mapX', 'mapY']
    for t in timeRangeLoop:
        newAllTimeValues = {}
        for k in variableKeyLoop:
            if k in allTime and k in yesterdaysNews:
                newAllTimeValues[k] = updateMean(allTime['clickCount'],
                                                allTime[t][k], yesterdaysNews[t][k], yesterdaysNews['clickCount'])
            plotData.update_one(
                {
                    'user': '!communityAllTime'
                },
                {'$set':
                    {
                        t: newAllTimeValues
                    }
                },
                {'$inc':
                    {
                        'clickCount': yesterdaysNews['clickCount']
                    }
                }
            )
    return

def setNewMeansDaily(oldMeans: dict, newData: dict):
    d = newData.dict()
    ct = oldMeans['clickCount']
    vals = oldMeans[newData.timerange]
    updated = {}
    fields = ['happiness', 'calm', 'mapX', 'mapY']
    for f in fields:
        updated[f] = updateMean(ct, vals[f], d[f], 1)
    return updated

def getAllUserData(user: str):
    return plotData.find({'user': user},{'_id': 0, 'user': 0})