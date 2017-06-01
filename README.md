Maxxbook Setup Guide
====================

There are two ways to run the development environment.

The first is by using virtualenv and the Flask dev server. This one is harder to set up but can be faster for development.

The second is by using Docker and docker-compose. This one is easier to set up and more accurate to prod but requires restarting the containers after every change.

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
3. 
4. `source venv/bin/activate`


4. `pip install -r requirements.txt`
5. `pip install -e .`

# Docker Setup

Please make sure the following are installed:

* Docker
* Docker-compose