from itertools import filterfalse
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from models.userModel import User,ActivationModel,ResetModel
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
import modules.AuthenticationModule as auth
from schemas.userSchema import parseUser

authenticator=OAuth2PasswordBearer(tokenUrl="api/auth/login")

authRoute=APIRouter(
    prefix="/api/auth",
    tags=['UserAuthentication'],
)

@authRoute.post('/register')
async def registerUser(newUser: User):
    await auth.addUserToDatabase(newUser)
    return {"success":True}
    

@authRoute.post('/login')
def loginUser( user: OAuth2PasswordRequestForm=Depends()): 
    checkedUser = auth.verifyUserAtLogin({'username': user.username, 'password': user.password})  
    if checkedUser==False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token=auth.createAccessToken(checkedUser['username'],{'days':0,'minutes':30})
    return {"access_token":token,"token_type":"bearer"}

@authRoute.post('/logout')
def logout(token: str = Depends(authenticator)):
    return {"delete":True}

@authRoute.post('/activate')
def activate(tokenDict:ActivationModel):
    newToken = auth.activateUser(tokenDict)
    return {"access_token":newToken, "token_type":"bearer"} 

@authRoute.post('/forgot')
async def sendResetEmail(email:ResetModel):
    await auth.sendResetEmail(email.email)
    return {'message':f"reset email sent to {email}"}

@authRoute.post('/reset')
def reset(newPassword:ResetModel):
    print(newPassword)
    auth.resetPassword(newPassword)
    return {'message':'password reset successful'}

@authRoute.post('/refresh')
def refresh(oldToken):
    newToken=auth.refreshToken(oldToken)
    return {'access_token':newToken,"token_type":"bearer"}