from flask import Flask
from flask.ext.login import login_required , current_user
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
import os
from werkzeug import secure_filename


app = Flask(__name__, instance_relative_config=True,static_url_path="/static")
db = SQLAlchemy(app)




app.config['SECRET_KEY'] = '$&^&B&*^*MN&*CDMN&*()B^&*()P^&_N*NM(P)*&D()&*^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:badman1108@localhost/blueflag'
app.debug = True



