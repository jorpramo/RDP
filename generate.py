__author__ = 'jpradas'
import random
import pymongo
import settings as set


client = pymongo.MongoClient(set.MONGO_URI)
db = client.rdp
rest=db.restaurantes
num=random.randint(1, 2500)

cursor=rest.find({"posicion": str(num)})[0]
#cursor=rest.find({"posicion": '2008'})
#print(cursor.count())
print(num)
print(cursor['nombre'])
