# -*- coding: utf-8 -*-

from flask import Blueprint, request, jsonify
from database import db
from .models import Movie, MovieSchema

bp = Blueprint("movies", __name__, url_prefix="/movies")

@bp.route("/")
def all():

    "Return all movies"
    
    movies = Movie.query.all()
    schema = MovieSchema(many=True)
    result = schema.dump(movies)
    return jsonify(dict(movies=result))

@bp.route("/<int:id>")
def get():

    "Return a movie"
    
    id = request.args.get("id")
    movie = Movie.query.filter_by(id=id).first()
    if not movie:
        return jsonify(dict(error="MOVIE NOT EXIST"))
    return jsonify(dict(movie=movie))

@bp.route("/", methods=["POST"])
def create():
    
    "Create a movie"

    title = request.get_json()["title"]
    if not title:
        return jsonify(dict(error="TITLE IS REQUIRED"))
    movie = Movie(title=title)
    db.session.add(movie)
    db.session.commit()
    schema = MovieSchema()
    result = schema.dump(movie)
    return jsonify(dict(movie=result)), 201

@bp.route("/<int:id>", methods=["PUT"])
def update(id):
    
    "Update a movie"

    movie = Movie.query.filter_by(id=id).first()
    movie.title = request.get_json()["title"]
    db.session.commit()
    schema = MovieSchema()
    result = schema.dump(movie)
    return jsonify(dict(movie=result))

@bp.route("/<int:id>", methods=["DELETE"])
def delete(id):

    "Delete a movie"
    
    movie = Movie.query.filter_by(id=id).first()
    db.session.delete(movie)
    db.session.commit()
    return "", 204
