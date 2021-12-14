# from routes.auth import gate
from fastapi import APIRouter, Depends
from models.plotModel import PlotDataSubmission,UserPlotData,UserColorChange
from modules.AuthenticationModule import gate
import modules.PlotDataModule as plot
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

plotRoute=APIRouter(
    prefix="/api/plot",
    tags=['PlotData'],
)

@plotRoute.post('/getplotclick')
def getPlotClick(clickData:PlotDataSubmission, user:str=Depends(gate)):
    return plot.filePlotClick(user,clickData)

@plotRoute.post('/usercolorchoice')
def getInitialColors(user:str=Depends(gate)):
    return plot.getUserColors(user)

@plotRoute.post('/changecolors')
def changeColor(colorChange:UserColorChange,user:str = Depends(gate)):
    return plot.changeUserColor(user,colorChange)

@plotRoute.get('/userclickdata')
def getUserClickData(user:str = Depends(gate)):
    return plot.getUserClickData(user)

@plotRoute.get('/communityclickdata')
def getCommunityClickData():
    return plot.getCommunityClickData()

@plotRoute.get('/listofcolors')
def sendColorList():
    return plot.getColorList()

@plotRoute.get('/popularcolors')
def getPopularColors():
    return plot.getPopularColors()

@plotRoute.get('/communitycolors/{variable}')
def getCommunityColors(variable:str):
    return plot.getCommunityColors(variable)
