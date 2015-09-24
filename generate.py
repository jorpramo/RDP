__author__ = 'jpradas'
import random
import pymongo
import settings as set
import numpy as np

client = pymongo.MongoClient(set.MONGO_URI)
db = client.rdp
rest=db.restaurantes
total=rest.find({}).count()

cursor=rest.find({"posicion": str(total)})

for c in cursor:
    print(c["nombre"])
c=[]
total=rest.find({}).sort("posicion",1)
for t in total:
    c.append(([t['posicion'].replace("\n", "").replace(".", ""), t["nombre"].replace("\n", "")]))

c=sorted(c, key=lambda res: c[0] ,reverse=True)

for lin in c:
    print(lin[0] + ";" + lin[1])