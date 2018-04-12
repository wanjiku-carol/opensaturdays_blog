from flask import json, request, jsonify
from flask_restful import Resource
from models import db, Todo


class TodoResource(Resource):
    """
    Create a Todo Resource with GET, POST, PUT and DELETE methods
    """

    def get(self):
        todos = Todo.query.all()
        response = [todo.json_dump() for todo in todos]
        return {"status": "success", "data": response}, 200

    def post(self):
        json_data = request.get_json(force=True)
        todo = Todo(name=json_data['name'])
        todo.save()
        response = json.dumps(todo.json_dump())
        return {"status": "success", "data": response}, 200
