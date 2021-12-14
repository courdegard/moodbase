from pydantic import BaseModel
from datetime import datetime,timezone

class WeightData(BaseModel):
    name:str
    value:int
    delta:int
