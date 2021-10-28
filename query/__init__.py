#Tutorial: https://www.youtube.com/watch?v=Qr4QMBUPxWo

from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_key"

app.config["RECAPTCHA_ENABLED"] = True
app.config["RECAPTCHA_PUBLIC_KEY"] = "6LfnbPocAAAAAMOeuW7aCWvWWmO7bGsyBxra-5tr"
app.config["RECAPTCHA_PRIVATE_KEY"] = "6LfnbPocAAAAANalES5ltkJEl3WReNcNmrUs5hv0"
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
#db = SQLAlchemy(app)

from query import routes