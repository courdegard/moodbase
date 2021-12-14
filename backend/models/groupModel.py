from pydantic import BaseModel

class GroupData(BaseModel):
    name:str
    memberDict:dict
    colors:dict
    weightButtons:dict
    adminUser:str
    timeInterval:int
    password:str