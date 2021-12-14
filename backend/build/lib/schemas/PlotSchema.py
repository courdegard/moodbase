from db import plotData
from datetime import datetime
from models.plotModel import PlotDataSubmission
from bson import Decimal128
# def createCommunityDocument(initialData:PlotDataSubmission):
#     plotData.insert_one(
#         {
#             'community':True,
#             'dayList':[datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)],
#             'mapX':[initialData.clickMap['happinessVal']],
#             'mapY':[initialData.clickMap['calmVal']],
#             'averageLineChartHappiness':[initialData.lineChart['happinessVal']],
#             'averageLineChartCalm':[initialData.lineChart['calmVal']],
#             'totalHappinessByDay':[initialData.lineChart['happinessVal']],    
#             'totalCalmByDay':[initialData.lineChart['calmVal']],
#             'clickCount':0   
#         }
#     )
#     return True

def createUserPlotDataDocument(user:str):
    clickData= { 
        'user':user,
        'happiness':[],
        'calm':[],
        'mapX':[],
        'mapY':[],
        'timestamp':[]
        }
    plotData.insert_one(clickData)
    return clickData

def updateUserPlotDataDocument(user:str,newData:PlotDataSubmission):
    plotData.update_one(
        {'user':user},        
            {
            '$push':
                {
                    'happiness':newData.lineChart['happinessVal'],
                    'calm':newData.lineChart['calmVal'],
                    'mapX':newData.clickMap['happinessVal'],
                    'mapY':newData.clickMap['calmVal'],
                    'timestamp':newData.timestamp
                },
            },
            upsert=True     
        )
    return True

def dumbDecimalThing(floatVal,decimal128Val,countVal):
    decimal2Float=float(str(decimal128Val))
    return Decimal128(str((floatVal+decimal2Float)/countVal))

def updateCommunityPlotData(newData:PlotDataSubmission):
    listOfValues=newData.returnList()
    i=0
    currentCommunityData = plotData.find_one({'community':True})
    clickCount=currentCommunityData['clickCount']+1
    if len(currentCommunityData['dayList'])<1 or currentCommunityData['dayList'][-1].day != datetime.now().replace(hour=0,minute=0,second=0,microsecond=0).day:
        createNewDay(listOfValues)
    else:
        index=len(currentCommunityData['dayList'])-1
        del currentCommunityData['_id']
        for key,value in currentCommunityData.items():
            if key[0]=="m":
                plotData.update_one(
                    {'community':True},
                    {'$set':
                        {key+'.'+str(index):dumbDecimalThing(listOfValues[i],value[index],clickCount)}
                    }
                )
                i+=1
            if key[0]=="a":
                plotData.update_one(
                    {'community':True},
                    {'$set':
                        {key+"."+str(index):dumbDecimalThing(listOfValues[i],value[index],clickCount)}
                    }
                )
                i+=1
            elif key[0]=='t':
                plotData.update_one(
                    {'community':True},
                    {'$inc':
                        {
                        'totalHappinessByDay.'+str(index):newData.lineChart['happinessVal'],
                        'totalCalmByDay.'+str(index):newData.lineChart['calmVal'],
                        }
                    }
                )
        plotData.update_one(
            {'community':True},
            {'$inc':
                {
                'clickCount':1
                }
            }
        )
            
    
    return True

def createNewDay(listOfValues:list):
    plotData.update_one({'community':True},
        {'$push':
            {
            'dayList':datetime.now().replace(hour=0,minute=0,second=0),
            'mapX':listOfValues[0],
            'mapY':listOfValues[1],
            'averageLineChartHappiness':listOfValues[2],
            'averageLineChartCalm':listOfValues[3],
            'totalHappinessByDay':listOfValues[2],
            'totalCalmByDay':listOfValues[3],
            },
        '$inc':
            {'clickCount':1}
        })
    return True