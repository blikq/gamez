from django.db import models
from pymongo import MongoClient
import json
# Create your models here.

key = MongoClient()
collection = key["gamez"]
converge_doc = collection["converge"]
fitgirl_doc = collection["fitgirl"]
steamunlocked_doc = collection["steamunlocked"]

#using steamunlocked

def create_and_update_names():
    names_1 = fitgirl_doc.find()
    names_2 = steamunlocked_doc.find()
    for cont in names_1:
        converge_doc.update_one({"name": cont["name"]}, {"$set": {"name": cont["name"], "content": []}}, upsert=True)
    for cont in names_2:
        converge_doc.update_one({"name": cont["name"]}, {"$set": {"name": cont["name"],  "content": []}}, upsert=True)

def create_and_update_name():
    check_if_exist = converge_doc.estimated_document_count()
    if check_if_exist == 0:
        create_and_update_names()

def update_content():
    ind = converge_doc.find()
    for i in ind:
        #DECIDED TO USE AHASJMAP METHOD
        # cont1 = fitgirl_doc.find_one({"name": i["name"]})
        # if cont1 is not None:
        #     converge_doc.update_one({"name": cont1["name"]}, {"$push": {"content": cont1}})

        # cont2 = steamunlocked_doc.find_one({"name": i["name"]})
        # if cont2 is not None:
        #     converge_doc.update_one({"name": cont2["name"]}, {"$push": {"content": cont2}})
        cont1 = fitgirl_doc.find_one({"name": i["name"]})
        if cont1 is not None:
            converge_doc.update_one({"name": cont1["name"]}, {"$set": {"fitgirl": cont1}})
            ###
        cont2 = steamunlocked_doc.find_one({"name": i["name"]})
        if cont2 is not None:
            converge_doc.update_one({"name": cont2["name"]}, {"$set": {"steamunlocked": cont2}})


create_and_update_names()
update_content()