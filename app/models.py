
from app import db
from slugify import slugify


class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    crop_type = db.Column(db.String(80), unique=False)
    slug = db.Column(db.String(80), unique=True)

    def __init__(self, name, crop_type):
        self.name = name
        self.crop_type = crop_type
        self.slug = slugify(name)

    def __repr__(self):
        return '<Crop %r>' % self.name
