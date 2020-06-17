import os
import ee

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_environments import Environments







app = Flask(__name__, instance_relative_config=True)

db = SQLAlchemy(app)
ma = Marshmallow(app)
env = Environments(app)
env.from_yaml(os.path.join(os.getcwd(), 'conf/main.yml'))

ee_api_config = app.config['EARTH_ENGINE_API']
private_key_file = os.path.join(os.getcwd(), ee_api_config['PRIVATE_KEY'])
service_account = os.path.join(os.getcwd(), ee_api_config['ACCOUNT'])

credentials = ee.ServiceAccountCredentials(service_account, private_key_file)


def create_app(test_config=None):

    @app.route('/')
    def hello():
        return 'API is working'


    from . import ndvi, evi, crops, chirps
    app.register_blueprint(ndvi.bp)
    app.register_blueprint(evi.bp)
    app.register_blueprint(crops.bp)
    app.register_blueprint(chirps.bp)

    return app
