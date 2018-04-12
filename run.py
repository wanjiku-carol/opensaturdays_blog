from flask import Flask
from flask_restful import Api
from app import Hello
from resources.todo import TodoResource
from resources.item import ItemResource


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    api = Api(app)

    from models import db
    db.init_app(app)

    api.add_resource(Hello, '/')
    api.add_resource(TodoResource, '/todo', '/todo/', '/todo/<string:id>',
                     '/todo/<string:id>/')
    api.add_resource(ItemResource, '/items')

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
