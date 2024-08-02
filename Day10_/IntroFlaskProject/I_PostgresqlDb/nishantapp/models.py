from nishantapp import db
from datetime import datetime
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(200),unique=True,nullable=False)
    password=db.Column(db.String(90),nullable=False)
    posts=db.relationship('Post',backref='author',lazy=True)

    def __repr__(self):
        return f"User(username={self.username},email={self.email})"

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
            return f"Post(title={self.title},date_posted={self.date_posted})"
