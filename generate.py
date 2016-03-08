__author__ = 'jpradas'
from flask import Flask,  request
from flask import render_template
import logging
import sys
import yelp_api

app = Flask(__name__)
# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sorteo/',methods=['POST'])
def sorteo():

    # la funcion dame_restaurante devuelve un registro de tipo business del api de yelp
    # https://www.yelp.com/developers/documentation/v2/business

    elegido=yelp_api.dame_restaurante(request.form['ciudad'])
    num=elegido[0].rating
    nombre=elegido[0].name

    return render_template('sorteo.html', num=num, nombre=nombre, imagen=elegido[0].image_url,url=elegido[0].url, telefono=elegido[0].display_phone, direccion=elegido[0].location.display_address )


if __name__ == '__main__':
    #admin = Admin(app, name='RandomDinnerProject: Listado', template_mode='bootstrap3')
    app.run()

