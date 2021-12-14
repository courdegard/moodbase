from fastapi import APIRouter, Depends
from models.weightModel import WeightData
import schemas.WeightSchema as weight
from modules.AuthenticationModule import gate

weightRoute=APIRouter(
    prefix="/api/allot",
    tags=['WeightData'],
)

@weightRoute.post('/updateweightdata')
def updateWeightData(data:WeightData,user:str=Depends(gate)):
    weight.updateWeightData(user=user,newData=data)
    return True

@weightRoute.get('/retrieveweightdata')
def retrieveWeightData(user:str=Depends(gate)):
    return weight.retrieveWeightData(user)
    
@weightRoute.post('/createnewbutton/{name}')
def createNewWeight(name:str,user:str=Depends(gate)):
    weight.createNewButton(name,user)
    return True

@weightRoute.post('/deletebutt/{name}')
def wipeButt(name:str,user:str=Depends(gate)):
    return weight.wipeButt(name,user)