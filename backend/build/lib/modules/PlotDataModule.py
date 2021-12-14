from db import plotData, colorData
from models.plotModel import PlotDataSubmission, UserColorChange
from schemas import PlotSchema, ColorSchema
import os
from bson import json_util
import json

def filePlotClick(user:str,data:PlotDataSubmission):
    data.truncateCoordinates()
    # if plotData.find({'community':True}).limit(1).countDocuments()<1:
    #     PlotSchema.createCommunityDocument(data)
    PlotSchema.updateUserPlotDataDocument(user,data)
    PlotSchema.updateCommunityPlotData(data)
    ColorSchema.getPopularColors()
    return True

def getUserClickData(user:str):
    if plotData.find({'user':user}).limit(1).count()<1:
        clickData=PlotSchema.createUserPlotDataDocument(user)
    else:
        clickData=plotData.find_one({'user':user},{'_id':0})
    return clickData

def getCommunityClickData():
    communityData = plotData.find_one({'community':True})
    del communityData['_id']
    del communityData['community']
    return json.loads(json_util.dumps(communityData))

def getUserColors(user:str):
    if colorData.find({'user':user}).limit(1).count()<1:
        return ColorSchema.createUserColorProfile(user)
    else:
        colorProfile = colorData.find_one({'user':user},{'_id':0})
        return colorProfile

def changeUserColor(user:str,changeData:UserColorChange):
    try:
        ColorSchema.updateUserColorProfile(user,changeData)
        return {'Message':'Color change successful'}
    except:
        return {'something happened':'color change failed'}

def getColorList():
    currentCategory='black'
    colors={'black':{},'gray':{},'blue':{},'green':{},
            'yellow':{},'brown':{},'orange':{},'red':{},
            'pink':{},'purple':{},'white':{}}
    with open(os.path.join(os.path.dirname(__file__),"ColorCombinations.csv")) as colorList:
        for color in colorList:
            readCSV=color.split(',')
            if readCSV[0]=="Category":
                currentCategory=readCSV[1].strip()
            else:
                colors[currentCategory][readCSV[0]]=readCSV[1].strip()
    return colors

def getPopularColors():
    return ColorSchema.getPopularColors()

def getCommunityColors(emotionVar:str):
    return ColorSchema.getColorAggregates(emotionVar)