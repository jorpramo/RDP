__author__ = 'jpradas'
import random
import pymongo
import settings as set


client = pymongo.MongoClient(set.MONGO_URI)
db = client.rdp
rest=db.restaurantes
num=random.randint(1, 1000)

cursor=rest.find({"posicion": str(num)})[0]

print(num)
print(cursor['nombre'])
