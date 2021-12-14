from typing import Optional
from db import userData
from pydantic import BaseModel, EmailStr, Field

class TestModel(BaseModel):
    testing:str

class User(BaseModel):
    username: str 
    password: str
    email: Optional[EmailStr]
    active= False

class ActivationModel(BaseModel):
    token:str

class ResetModel(BaseModel):
    email:Optional[EmailStr]
    token:Optional[str]
    newPassword:Optional[str]