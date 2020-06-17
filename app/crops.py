from app import credentials
from gzipped import gzipped
from flask_cors import cross_origin

from app.models import Crop
from app.schema import CropSchema

from flask import Blueprint, jsonify


bp = Blueprint('crops', __name__, url_prefix='/crops')
EE_CREDENTIALS = credentials


@bp.route('/', methods=["GET"])
@gzipped
@cross_origin()
def index():

    crop = Crop.query.all()

    response = {
        'success': True
    }

    crop_schema = CropSchema(many=True)
    result = crop_schema.dump(crop)
    response['result'] = result

    return jsonify(response)
