# -*- coding: utf-8 -*-

import os

class Config(object):

   DEBUG = False
   TESTING = False
   SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):

   DEBUG = True
   SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
                             os.path.abspath(os.path.join(os.path.dirname(__name__), "dev.db"))


class ProductionConfig(Config):

      SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
                             os.path.abspath(os.path.join(os.path.dirname(__name__), "app.db"))
