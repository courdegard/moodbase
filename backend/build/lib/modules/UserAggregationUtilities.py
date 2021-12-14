from db import userData

def updateUserCountOnActivation():
    try:
        userData.update_one({'isUserCount':True}, {'$inc':{'count':1} })
    except:
        userData.insert_one({'isUserCount':True,'count':1})

def getNumberOfUsers():
    try:
        return userData.find_one({'isUserCount':True})['count']
    except:
        return False