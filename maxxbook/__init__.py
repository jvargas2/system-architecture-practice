from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from maxxbook.config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


app.config.from_envvar('FLASKR_SETTINGS', silent=True)

import maxxbook.views

if __name__ == "__main__":
	app.run()