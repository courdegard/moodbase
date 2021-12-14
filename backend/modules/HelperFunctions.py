from datetime import datetime, timedelta

def returnDay():
    d = datetime.utcnow()
    return d.replace(hour=0,minute=0,second=0,microsecond=0)

def getYesterday(day):
    return day - timedelta(1)