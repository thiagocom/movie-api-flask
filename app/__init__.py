# -*- coding: utf-8 -*-

from flask import Flask
from . import movies
from database import db

def create_app(config_class=None):

   "Factory app"

   # App
   app = Flask("app")
   
   # Configuration
   app.config.from_object(config_class)
   
   # Register blueprint
   app.register_blueprint(movies.bp)

   # Initialize database
   db.init_app(app)

   return app
