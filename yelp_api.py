__author__ = 'Jorge'

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import io,json
from random import randint


# read API keys
with io.open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

client = Client(auth)

#offset=1&limit=1&cc=ES&lang=es&category_filter=restaurants

def dame_restaurante(ciudad):
    params = {
        'term': 'food',
        'lang': 'es',
        'limit': 1,
        'category_filter': 'restaurants'
    }

    response = client.search(ciudad, **params)
    if response.total>=1000:
        params['offset']=str(randint(1, 999))


    else:
        params['offset']=str(randint(1, response.total))

    response = client.search(ciudad, **params)
    for rest in response.businesses:
        print(rest.id)
        print(rest.name)
        print(rest.rating)
    return response.businesses

'''
elegido=client.get_business('la-gabinoteca-madrid')
print(elegido.business.phone)
'''

#dame_restaurante("Valencia")