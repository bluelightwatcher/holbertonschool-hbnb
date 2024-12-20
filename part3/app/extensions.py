from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt() 
jwt = JWTManager()
db = SQLAlchemy()
