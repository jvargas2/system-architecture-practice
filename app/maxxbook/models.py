from datetime import datetime
from maxxbook import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    first_name = db.Column(db.String(80), unique=False)
    last_name = db.Column(db.String(80), unique=False)
    password = db.Column(db.String(80), unique=False)
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    created_at = db.Column(db.DateTime, unique=False)

    def __init__(self, email, first_name, last_name, password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<User %r %r>' % (self.first_name, self.last_name)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    def __init__(self, user_id, body):
        self.user_id = user_id
        self.body = body
        self.pub_date = datetime.utcnow()

    def __repr__(self):
        return '<Post %r>' % str(self.id)