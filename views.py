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
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filename)
            return render_template('upload.html',alert='File Uploaded Succesfully!')
    return render_template('upload.html')


if __name__ == '__main__':
	app.run('0.0.0.0')