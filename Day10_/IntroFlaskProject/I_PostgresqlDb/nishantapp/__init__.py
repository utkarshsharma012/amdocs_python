from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app=Flask(__name__)#wsgi_app_object=Flask('modulename')
app.config['SECRET_KEY']='01a51da4f5e0edf92c3140a55361a97c'
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='nishant',pw='1234',url='127.0.0.1',db='learning')
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db=SQLAlchemy()
db.init_app(app)
app.app_context().push()

from nishantapp import routes

with app.app_context():
    db.create_all()
    print('Database & Tables created!')
