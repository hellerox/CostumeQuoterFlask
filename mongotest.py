from pymongo import MongoClient

client = MongoClient('mongodb+srv://carlos:alfredo@cluster0-qkumg.gcp.mongodb.net/ACdev?retryWrites=true')

db = client['ACdev']

import datetime

material =  {
        "nombrematerial": "Terciopelo Bermejo",
        "idtipomaterial": 1,
        "idmedidamaterial": 1,
        "costo": 104
    }

record_id = db.materials.insert(material)

print (record_id)
print (db.collection_names())

materials = db.materials
output = []
print("total:",materials.count())