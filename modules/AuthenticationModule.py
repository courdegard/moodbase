# database stuff
from db import userData


from models.userModel import User

# email stuff
import modules.EmailModule as email

# dependency injection stuff
from fastapi import HTTPException, Depends,BackgroundTasks

# jwt and password stuff
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime,timedelta,timezone
from dotenv import load_dotenv
load_dotenv('.env')
from decouple import config

secret=config('secret')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# decode token
# determine if token is still valid
# create refresh token if within 10sec of expiry
# return either access or refresh token
def checkToken(token):
    decoded = jwt.decode(token, secret, 'HS256')
    issued=datetime.fromtimestamp(decoded['iat'],tz=timezone.utc)
    now=datetime.now(timezone.utc)
    if (now-issued)<(now-(now-timedelta(seconds=10))):
        return createAccessToken(decoded['sub'],{'days':0,'minutes':2})
    else: 
        return token
        

def verifyUserAtLogin(loginAttempt):
    checkUsername={'username':loginAttempt['username']}
    if userData.find(checkUsername).limit(1).count()<1:
        return False
    else:
        userToCheck=userData.find_one(checkUsername)
        if pwd_context.verify(loginAttempt['password'].encode('utf-8'), userToCheck['password']):
            return userToCheck
        else:
            return False    

def createAccessToken(subName,duration):
    payload = {
        'exp' : datetime.now(timezone.utc) + timedelta(days=duration['days'], minutes=duration['minutes']),
        'iat' : datetime.now(tz=timezone.utc),
        'sub' : subName        }
    return jwt.encode(
        payload, 
        secret,
        algorithm='HS256'
    )

def addUserToDatabase(user):
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
        activationToken=createAccessToken(user.username,{'days':2,'minutes':0})
        url=createUrlForEmail("activate",activationToken)
        activationSpecs={'urlDict':{'url':url},'subject':'Activation email','recipient':user.email,'template':'ActivationEmail.html'}
        return activationSpecs

def getUserFromToken(token):
    decoded = jwt.decode(token, secret, 'HS256')
    userStr=decoded['sub']
    user = userData.find_one({'username':userStr})
    return user

def createUrlForEmail(route,token):
    url=f"http://localhost:8080/{route}/{token}"
    return url

def activateUser(tokenDict):
    user=getUserFromToken(tokenDict.token)
    userData.update_one(user,{'$set':{'active':True}})
    returnToken=createAccessToken(user['username'],{'minutes':2})
    return returnToken

def sendResetEmail(emailObj):
    lookupEmail={'email':emailObj.email}
    user=userData.find_one(lookupEmail)
    forgotToken=createAccessToken(user['username'],{'days':0,'minutes':60})
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
    
