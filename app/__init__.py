# -*- coding: utf-8 -*-

from flask import Flask

def create_app():

	"Factory app"

	app = Flask("app")

	return app