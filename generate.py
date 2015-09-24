__author__ = 'jpradas'
import random
import pymongo
import settings as set

client = pymongo.MongoClient(set.MONGO_URI)
db = client.rdp
rest=db.restaurantes
total=rest.find({}).count()

print(random.randint(1, total))

cursor=rest.find({"posicion": str(total)})

for c in cursor:
    print(c["nombre"])

