from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash



db = SQLAlchemy()
ma = Marshmallow()
mg = Migrate()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(800))

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=2)
    
    def check_password(self, pas):
        return check_password_hash(self.password, pas)



class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
