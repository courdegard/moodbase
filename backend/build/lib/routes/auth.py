from itertools import filterfalse
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks, Request, Header, Security
from fastapi.responses import JSONResponse
from models.userModel import User,ActivationModel,ResetModel,TestModel
import modules.AuthenticationModule as auth
import modules.EmailModule as email
from schemas.userSchema import parseUser


authRoute=APIRouter(
    prefix="/api/auth",
    tags=['UserAuthentication'],
)

@authRoute.post('/register')
async def registerUser(newUser: User,background_tasks:BackgroundTasks):
    emailToSend=auth.addUserToDatabase(newUser)
    background_tasks.add_task(email.sendEmailBackground,emailToSend)
    return 

@authRoute.post('/login')
def loginUser( user: User ): 
    checkedUser = auth.verifyUserAtLogin({'username': user.username, 'password': user.password})  
    if checkedUser==False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token=auth.createAccessToken(user.username,0,0,3)
    refresh_token=auth.createAccessToken(user.username,0,8,1)
    return {"access_token":access_token,'token_type':'bearer','refresh_token':refresh_token}

@authRoute.get('/refresh')
async def sendNewToken(refresh=Header(None), check_token=Header(None)):
    try:
        auth.getUserFromToken(check_token)
        return {'access_token':check_token,'token_type':'bearer'}
    except: 
        try: 
            return auth.attemptRefresh(refresh)
        except:
            raise HTTPException(status_code=401,detail='invalid token')

@authRoute.post('/logout')
def logout(refresh:str = Header(None),user: str = Depends(auth.gate)):
    auth.banKeyTTL(refresh)
    return {"delete":True}

@authRoute.post('/activate')
def activate(tokenDict:ActivationModel):
    newToken = auth.activateUser(tokenDict)
    return {"access_token":newToken, "token_type":"bearer"} 

@authRoute.post('/forgot')
async def sendResetEmail(emailObj:ResetModel,background_tasks:BackgroundTasks):
    emailToSend=auth.sendResetEmail(emailObj)
    background_tasks.add_task(email.sendEmailBackground,emailToSend)
    return {'message':f"reset email sent"}

@authRoute.post('/reset')
def reset(newPassword:ResetModel):
    auth.resetPassword(newPassword)
    return {'message':'password reset successful'}

