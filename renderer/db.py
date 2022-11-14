from pymongo import MongoClient
import time
from random import randint

key = MongoClient()
collection = key["gamez"]
converge_doc = collection["converge"]
features_doc = collection["features"]

def how_many():
    return converge_doc.estimated_document_count()

def get_cont_with_id(id):
    # if len(id) != 7:
    #     return None
    cont = []
    for c3 in id:
        con = converge_doc.find_one({"id": c3})
        con["name"] = con["name"].title()
        cont.append(con)
    return cont

def geneate_rand_for_rand():
    count = 0
    hot_list = []
    while count < 7:
        for_hot = randint(1, how_many())
        if for_hot in hot_list:
            pass
        else:
            hot_list.append(for_hot)
            count += 1
    return hot_list

def update_featured():
    rend = []
    count = 0
    while count < 8:
        rand = randint(1, how_many())
        if rand in rend:
            pass
        rend.append(rand)
        count += 1
    c_time = int(time.time())
    rend.append(c_time)
    features_doc.insert_one({"featuered": rend})

def get_featured():
    #8
    cont = features_doc.find_one()
    if cont == None:
        update_featured()    
    elif cont is not None:
        c_time = int(time.time())
        if c_time-cont["featuered"][-1] >= 86400:
            update_featured()

def op_featured():
    get_featured()
    cont = features_doc.find_one()
    return cont["featuered"][0:8]

