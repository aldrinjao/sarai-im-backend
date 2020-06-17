import os
import ee

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


service_account = 'sarai-522@decoded-academy-219803.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(
    service_account, 'privatekey.json')

app = Flask(__name__, instance_relative_config=True)


db = SQLAlchemy(app)
ma = Marshmallow(app)


def create_app(test_config=None):

    # create and configure the app

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://deploy:sarai111@localhost/sarai_maps_db'
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    from . import ndvi, evi, crops, chirps
    app.register_blueprint(ndvi.bp)
    app.register_blueprint(evi.bp)
    app.register_blueprint(crops.bp)
    app.register_blueprint(chirps.bp)

    return app
