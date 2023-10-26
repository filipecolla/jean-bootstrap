from app import db
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.sql import func

class Clinica(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    