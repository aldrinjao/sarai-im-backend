from app import ma
from .models import Crop


class CropSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Crop
