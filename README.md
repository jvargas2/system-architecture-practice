Maxxbook Setup Guide
====================

# Virtualenv Setup

Please make sure the following are installed:

* Python 3.6 - The programming language the whole project will be using
* Pip3 - A python package manager
* Virtualenv - A tool for creating isolated python environment so you're installing every package globally
* PostgreSQL - The database the project will be using

Set up your database

1. Start your Postgres server and make sure it's running on port 5432
2. Create a database named `maxxbook_dev`


Run the following commands from the app directory to set up virtualenv:

1. `cd app`
2. `virtualenv venv`

Add the following lines to `venv/bin/activate` so you have the proper env variables:

* `export FLASK_APP='maxxbook'`
* `export FLASK_DEBUG='True'
* `export FLASK_DATABASE_URI="postgres://[your-postgres-username]@localhost:5432/maxxbook_dev"`

Activate the virtualenv and install the requirements:

1. `source venv/bin/activate`
2. `pip install -r requirements.txt`
3. `pip install -e .`

Start the app:
1. `flask run`
