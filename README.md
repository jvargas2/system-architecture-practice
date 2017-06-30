System Architecture Practice
====================

This repo is so I can practice building scalable architectures locally. I will be using docker-compose to emulate
a distributed system. The following are instructions for how to run the project yourself.

# Docker-compose Setup

Please make sure the following are installed:

* Docker
* Docker-compose

Run the following command to start your docker containers:

`docker-compose up`

Here are some other useful commands for running the project:

* To rebuild the containers: `docker-compose up --build`
* To run the containers in the background: `docker-compose up -d`
* To see which containers are running: `docker ps`
* To shut down the containers: `docker-compose kill`
* To destroy the containers: `docker-compose down`
