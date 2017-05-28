from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from maxxbook.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    body = Column(Text)
    pub_date = Column(DateTime)

    # category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    # category = db.relationship('Category',
    #     backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        # self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title