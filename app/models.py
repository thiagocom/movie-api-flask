# -*- coding: utf-8 -*-

from database import db
from marshmallow import Schema, fields

class Movie(db.Model):

   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String)

   def __repr__(self):
      return "<Movie: {}>".format(self.title)


class MovieSchema(Schema):

	id = fields.Int()
	title = fields.Str()
