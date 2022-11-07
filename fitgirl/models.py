from django.db import models
from pymongo import MongoClient

# Create your models here.

db = MongoClient()
cluster = db["gamez"]
fitgirl_dbase = cluster["fitgirl"]
# a = {'name': name, 'version': version, 'date_released': date_re, 'originalSize': or_size, 'repackSize': re_size, "link": link, 
#         'selective': selective, 'genres': genres, 'companies': companies, 'languages': lang, 'screenshots': screenshot}
# name:str, version:str, date_re:str, or_size:str, re_size:str, selective:bool, genres:list, link, companies:list, lang:list, screenshot:list

def fitgirl_db(a):
    fitgirl_dbase.insert_many(a)
