from django.db import models
from pymongo import MongoClient

# Create your models here.
db = MongoClient()
cluster = db["gamez"]
su_dbase = cluster["steamunlocked"]

def steamun_db(a):
    try:
        su_dbase.insert_many(a)
    except:
        return False
