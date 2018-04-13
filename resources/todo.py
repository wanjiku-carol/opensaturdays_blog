from flask import json, request
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
        response = json.loads(json.dumps(todo.json_dump()))
        return {"status": "success", "data": response}, 201

    def put(self, id):
        json_data = request.get_json(force=True)
        todo = Todo.query.filter_by(id=id).first()
        todo.name = json_data['name']
        db.session.commit()
        response = todo.json_dump()
        return{"status": "success", "data": response}, 200

    def delete(self, id):
        json_data = request.get_json(force=True)
        Todo.query.filter_by(id=id).delete()
        db.session.commit()
        response = json.loads(json.dumps(json_data))
        return {"status": "deleted", "data": response}, 200
