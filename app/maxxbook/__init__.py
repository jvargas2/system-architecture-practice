from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from maxxbook.config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

import maxxbook.views

if __name__ == "__main__":
	app.run()