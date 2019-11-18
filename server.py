# -*- coding: utf-8- *-

import os
from app import create_app
from database import db
from app.models import Movie
from config import Config, DevelopmentConfig

def select_config(env):

   config_class = Config
   if env == "development":
      config_class = DevelopmentConfig
   return config_class

environ = os.getenv("FLASK_ENV")
config_class = select_config(environ)

app = create_app(config_class)

@app.shell_context_processor
def make_shell_context():
	return dict(db=db, Movie=Movie)
