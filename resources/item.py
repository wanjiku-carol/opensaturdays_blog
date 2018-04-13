import json
from flask import jsonify, request, make_response
from flask_restful import Resource
from models import db, Todo, Item


class ItemResource(Resource):
    """ Get all items belonging to one todo """

    def get(self, todo_id):
        items = Item.query.filter_by(todo_id=todo_id)
        response = [item.json_dump() for item in items]
        return {"status": "success", "data": response}, 200

    """ Create an item belonging to a todo """

    def post(self, todo_id):
        json_data = request.get_json()
        item = Item.query.filter_by(todo_id=todo_id).first()
        item = Item(item=json_data['item'], todo_id=todo_id)
        item.save()
        response = json.loads(json.dumps(item.json_dump()))
        return {"status": "success", "data": response}, 201

    """ Update an item """
    def put(self, id, todo_id):
        json_data = request.get_json()
        item = Item.query.filter_by(id=id).first()
        item = Item(item=json_data['item'], todo_id=todo_id)
        item.save()
        response = json.loads(json.dumps(item.json_dump()))
        return {"status": "success", "data": response}, 200
