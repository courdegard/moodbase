from pydantic import BaseModel
from datetime import datetime

class WeightData(BaseModel):
    name:str
    value:int
    delta:int
    timerange:str
