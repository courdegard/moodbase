# database stuff
from db import userData,bannedKeys


from models.userModel import User

# email stuff
import modules.EmailModule as email

# dependency injection stuff
from fastapi import HTTPException, Depends,BackgroundTasks, Security, Header
# jwt and password stuff
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime,timedelta,timezone

from config import Secret
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from dotenv import load_dotenv
load_dotenv('.env')
from decouple import config

security = HTTPBearer()

secret=config('secret')
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gate(refresh: str = Header(None), userAuth: HTTPAuthorizationCredentials = Security(security)):
    try:
        user=getUserFromToken(userAuth.credentials)
        return user
    except:
        raise HTTPException(status_code=401,detail='invalid token')

def verifyUserAtLogin(loginAttempt: User) -> User:
    checkUsername={'username':loginAttempt['username']}
    if userData.find(checkUsername).limit(1).count()<1:
        return False
    else:
        userToCheck=userData.find_one(checkUsername)
        if pwd_context.verify(loginAttempt['password'].encode('utf-8'), userToCheck['password']):
            return userToCheck
        else:
            return False    

def createAccessToken(subName: str,*args) -> dict():
    payload = {
        'exp' : datetime.now(timezone.utc) + timedelta(days=args[0], hours=args[1], minutes=args[2]),
        'iat' : datetime.now(tz=timezone.utc),
        'sub' : subName        }
    return jwt.encode(
        payload, 
        secret,
        algorithm='HS256'
    )

def getUserFromToken(checkToken:str)-> str:
    # print(checkToken)
    decoded = jwt.decode(checkToken, secret, 'HS256')
    userStr=decoded['sub']
    return userStr

    
def addUserToDatabase(user:User) -> dict:
    checkUsername={'username':user.username}
    # checkEmail={'email':user.email}
    # use find.limit instead of find_one because find will return whether or not doc exists
    # and find_one will return the whole doc
    if userData.find(checkUsername).limit(1).count()>0:
        raise HTTPException(status_code=404,detail="User already exists with this ID or email address")
    else: 
        userToDB=user.dict()
        userToDB['password']=pwd_context.hash(user.password)
        userData.insert_one(userToDB)
        activationToken=createAccessToken(user.username,2,0,0)
        url=createUrlForEmail("activate",activationToken)
        activationSpecs={'urlDict':{'url':url},'subject':'Activation email','recipient':user.email,'template':'ActivationEmail.html'}
        return activationSpecs

def createUrlForEmail(route: str,token:str) -> str:
    url=f"http://localhost:8080/{route}/{token}"
    return url

def activateUser(tokenDict: dict) -> dict:
    user=getUserFromToken(tokenDict.token)
    userData.update_one(user,{'$set':{'active':True}})
    returnToken=createAccessToken(user['username'],0,0,30)
    return returnToken

def sendResetEmail(emailObj):
    lookupEmail={'email':emailObj.email}
    user=userData.find_one(lookupEmail)
    forgotToken=createAccessToken(user['username'],0,0,60)
    url=createUrlForEmail("reset",forgotToken)
    emailSpecifications={'recipient':emailObj.email,'urlDict': {'url':url},'subject':"Reset password email",
    'template':'ResetEmail.html'}
    return emailSpecifications


def resetPassword(newPassword):
    resetToken=newPassword.token
    user=getUserFromToken(resetToken)
    if not user: raise HTTPException(status_code=404,detail='Did not work') 
    userData.update_one(user,{'$set':{'password':pwd_context.hash(newPassword.newPassword)}})
    return {'message':'password reset successfully'}

def attemptRefresh(refreshToken):
    # print(refreshToken)
    user=getUserFromToken(refreshToken)
    if user:
        return {'access_token':createAccessToken(user,0,0,1),'token_type':'bearer'}
    else:
        raise HTTPException(status_code=401,detail='invalid token')
        
def banKeyTTL(tokenToBan):
    try:
        expiry = createTTL(tokenToBan)
        bannedKeys.insert_one({'expires':expiry,'tokenValue':tokenToBan})
        return True
    except:
        raise HTTPException(status_code=418, detail="Something happened")

def createTTL(token:str):
    decoded = jwt.decode(token,secret,'HS256')
    expDT = datetime.fromtimestamp(decoded['exp'],tz=timezone.utc)
    return expDT
    # timeToExpire = (expDT - datetime.now(timezone.utc)).total_seconds()
    # return timeToExpire