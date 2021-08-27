# database stuff
from db import userData

# email stuff
import modules.EmailModule as email

# dependency injection stuff
from fastapi import HTTPException, Depends

# jwt and password stuff
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime,timedelta
from dotenv import load_dotenv
load_dotenv('.env')
from decouple import config

secret=config('secret')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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

def createAccessToken(subName):
    payload = {
        'exp' : datetime.utcnow() + timedelta(days=0, minutes=30),
        'iat' : datetime.utcnow(),
        'sub' : subName        }
    return jwt.encode(
        payload, 
        secret,
        algorithm='HS256'
    )

def addUserToDatabase(user):
    checkUsername={'username':user.username}
    checkEmail={'email':user.email}
    # use find.limit instead of find_one because find will return whether or not doc exists
    # and find_one will return the whole doc
    if userData.find(checkUsername).limit(1).count()>0 or userData.find(checkEmail).limit(1).count()>0:
        raise HTTPException(status_code=404,detail="User already exists with this ID or email address")
    else: 
        userToDB=user.dict()
        userToDB['password']=pwd_context.hash(user.password)
        userData.insert_one(userToDB)
        url=createUrlForEmail(user.username)
        return email.send_email_async(url=url,subject="Activation email",recipient=checkEmail['email'],template="ActivationEmail.html")

def getUserFromToken(token):
    decoded = jwt.decode(token, secret, 'HS256')
    userStr=decoded['sub']
    user = userData.find_one({'username':userStr})
    return user

def createUrlForEmail(username):
    token=createAccessToken(username)
    url=f"http://localhost:8080/home/{token}"
    return url

