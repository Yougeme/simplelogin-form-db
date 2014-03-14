from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  googleid = db.Column(db.String(64), index = True, unique = True)
  firstname = db.Column(db.String(64))
  lastname = db.Column(db.String(64))
  email = db.Column(db.String(120))
  role = db.Column(db.SmallInteger, default = ROLE_USER)
  posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

  def __repr__(self):
    return '<User %r>' % (self.firstname+self.lastname)

class Post(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  text = db.Column(db.String(140))
  boolean = db.Column(db.Boolean)
  select = db.Column(db.String(140))
  timestamp = db.Column(db.DateTime)
  integer = db.Column(db.Integer)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __repr__(self):
    return '<Post %r>' % (self.text)
