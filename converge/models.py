from django.db import models
from pymongo import MongoClient
import json
# Create your models here.

key = MongoClient()
collection = key["gamez"]
converge_doc = collection["converge"]
fitgirl_doc = collection["fitgirl"]
steamunlocked_doc = collection["steamunlocked"]
# genres = collection["genres"]

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
        #DECIDED TO USE HASHMAP METHOD
        # cont1 = fitgirl_doc.find_one({"name": i["name"]})
        # if cont1 is not None:
        #     converge_doc.update_one({"name": cont1["name"]}, {"$push": {"content": cont1}})

        # cont2 = steamunlocked_doc.find_one({"name": i["name"]})
        # if cont2 is not None:
        #     converge_doc.update_one({"name": cont2["name"]}, {"$push": {"content": cont2}})
        cont1 = fitgirl_doc.find_one({"name": i["name"]})
        if cont1 is not None:
            converge_doc.update_one({"name": cont1["name"]}, {"$set": {"fitgirl": cont1, "main_pic": cont1["screenshots"]}})
            ###
        cont2 = steamunlocked_doc.find_one({"name": i["name"]})
        if cont2 is not None:
            converge_doc.update_one({"name": cont2["name"]}, {"$set": {"steamunlocked": cont2, "main_pic": cont2["pictures"]}})
        

# def for_genres():
#     cont1 = fitgirl_doc.find()
    # for i in cont1:
    #     for g in i["genres"]:
    #         f = genres.find_one({"genres": [g]})
    #         if f == None:
    #             genres.update_one({"genres": []}, {"$push": {"genres": g.lower()}})

def number_converge():
    con = converge_doc.find()
    count = 1
    for i in con:
        converge_doc.update_one(i, {"$set": {"id": count}})
        count += 1

def get_genres():
    genres = converge_doc.find({"fitgirl": {"$exists": True}})
    genres_set = []
    for i in genres:
        if i["fitgirl"]["genres"] is not None:
            for n in i["fitgirl"]["genres"]:
                genres_set.append(n.lower())
    genres_set = set(genres_set)
    print(genres_set)
    
# print(converge_doc.find_one({"fitgirl": {"$exists": True}, "steamunlocked": {"$exists": True}}))

# get_genres()
# create_and_update_names() #1
update_content() #2
# for_genres()
# number_converge() #3
# get_genres()