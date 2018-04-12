import json
from flask import jsonify, request, make_response
from flask_restful import Resource
from models import db, Todo, Item


class ItemResource(Resource):
    """ Get all items belonging to one todo """

    def get(self):
        items = Item.query.all()
        results = []
        for item in items:
            results.append(obj)
            return make_response(jsonify(results)), 200
