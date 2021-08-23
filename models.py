from db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # contains image buffer data
    species = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, unique=True, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
