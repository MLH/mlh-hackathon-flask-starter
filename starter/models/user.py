from starter.db import get_db

db = get_db()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return "<User: {}>".format(self.username)
