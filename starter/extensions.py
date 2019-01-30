"""Database module"""
from flask_sqlalchemy import SQLAlchemy
from flask_misaka import Misaka

db = SQLAlchemy()
markdown = Misaka(fenced_code=True, tables=True, autolink=True, strikethrough=True, no_intra_emphasis=True)
