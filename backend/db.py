from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv('.env')
from decouple import config

conn = MongoClient(config('conn'))
db=conn['mbdata']
userData=db['Users']
plotData=db['PlotData']
colorData=db['ColorChoices']
bannedKeys=db['BannedKeys']
aggregateData=db['AggregateData']
weightData=db['WeightData']
weightPopularityData=db['WeightPopularityData']
groupData=db['GroupData']