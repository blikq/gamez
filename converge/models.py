from django.db import models
from pymongo import MongoClient

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
    name = []
    for cont1 in names_1:
        pop = converge_doc.find({"name": cont1["cont1"]})
        if pop != None:
            pass
        else:
            if pop["name"].lower() == cont1["name"].lower():
                pass

def create_and_update_name():
    check_if_exist = converge_doc.estimated_document_count()
    if check_if_exist == 0:
        create_and_update_names()
    
print(create_and_update_name())