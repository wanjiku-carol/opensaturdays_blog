from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(),
        nullable=False)
    todo_id = db.Column(db.Integer, db.ForeignKey(
        'todos.id', ondelete='CASCADE'), nullable=False)
    todo = db.relationship('Todo', backref=db.backref('items',
                                                      lazy='dynamic'))

    def __init__(self, item, todo_id):
        self.item = item
        self.todo_id = todo_id


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, name):
        """ Initialize with name of todo """
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all(todo_id):
        """Return all items belonging to a todo."""
        return Item.query.filter_by(belongs_to=todo_id)
