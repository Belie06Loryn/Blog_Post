from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager,db

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    pic = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))    

    def __repr__(self):
        return f'User {self.username}'

class Blogs(db.Model):
    __tablename__ = 'blogers'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    texto = db.Column(db.String(255))

    def ububiko(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls):
        blogers = Blogs.query.all()
        return blogers

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    blogerss = db.Column(db.Integer,db.ForeignKey('blogers.id'))

    @classmethod
    def get_comments(cls,blogerss):
        comments = Comment.query.filter_by(blogerss=blogerss).all()
        return comments