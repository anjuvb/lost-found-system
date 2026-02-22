from . import db

class User(db.Model):
    __tablename__ = "USER"
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(15))
    password = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey("ROLE.role_id"))