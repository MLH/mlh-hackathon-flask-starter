from starter.extensions import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    avatar_url = db.Column(db.String(80), nullable=True)
    github_id = db.Column(db.Integer(), nullable=True)

    def __init__(self, username, avatar_url, github_id):
        self.username = username
        self.avatar_url = avatar_url
        self.github_id = github_id

    def __repr__(self):
        return "<User: {}>".format(self.username)
