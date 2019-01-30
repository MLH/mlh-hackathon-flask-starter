"""Database module"""
from flask_sqlalchemy import SQLAlchemy
from flask_misaka import Misaka

db = SQLAlchemy()
markdown = Misaka()
