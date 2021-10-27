#Tutorial: https://www.youtube.com/watch?v=Qr4QMBUPxWo

from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
#db = SQLAlchemy(app)

from query import routes