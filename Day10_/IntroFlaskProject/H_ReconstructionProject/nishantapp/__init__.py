from flask import Flask


app=Flask(__name__)#wsgi_app_object=Flask('modulename')
app.config['SECRET_KEY']='01a51da4f5e0edf92c3140a55361a97c'

from nishantapp import routes
