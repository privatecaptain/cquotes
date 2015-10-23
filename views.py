from flask import Flask , make_response, render_template, jsonify, send_from_directory,request,redirect
from flask.ext.login import login_required , current_user
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func, select
import os
from werkzeug import secure_filename
import json
import random
from config import *


app = Flask(__name__, instance_relative_config=True,static_url_path="/static")
db = SQLAlchemy(app)




app.config['SECRET_KEY'] = '$&^&B&*^*MN&*CDMN&*()B^&*()P^&_N*NM(P)*&D()&*^'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.debug = True

class Quote(db.Model):

	id = db.Column(db.Integer, primary_key = True, autoincrement=True)

	content = db.Column(db.Text)
	author = db.Column(db.String(254))
	category = db.Column(db.String(254))

	def __init__(self):
		pass




@app.route('/')
def index():
	quotes = Quote.query.all()[:20]
	return render_template('index.html',quotes=quotes)


@app.route('/random')
def reply():
	print request.remote_addr
	while True:
		quote = Quote.query.order_by(func.rand()).first()
		if len(quote.content) < 150:
			break

	q = {}
	q['content'] = quote.content
	q['author'] = quote.author
	return json.dumps(q)

def getRandom():
	return random.randint(4000,6999)


if __name__ == '__main__':
	app.run('0.0.0.0')