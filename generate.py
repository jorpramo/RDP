__author__ = 'jpradas'
import random
import pymongo
import settings as set
from flask import Flask, redirect, request, url_for
from flask import render_template
import logging
import sys


app = Flask(__name__)
# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sorteo/')
def sorteo():

    client = pymongo.MongoClient(set.MONGO_URI)
    db = client.rdp
    rest=db.restaurantes

    #cursor=rest.find({"posicion": num})[0]
    conteo=0
    while (conteo==0):
        num=str(random.randint(1, 2500))
        cursor=rest.find({"posicion": num})
        conteo=cursor.count()
    nombre=cursor[0]['nombre']
    return render_template('sorteo.html', num=num, nombre=nombre)


if __name__ == '__main__':
    #admin = Admin(app, name='RandomDinnerProject: Listado', template_mode='bootstrap3')
    app.run()

