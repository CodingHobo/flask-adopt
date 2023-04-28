"""seed file for sample data for adopt database"""
from models import Pet, db
from app import app

db.create_all()
