from flask import Flask
from flask_restful import Api
from app import Hello


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    api = Api(app)

    from models import db
    db.init_app(app)

    api.add_resource(Hello, '/')

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
