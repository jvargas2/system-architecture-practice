FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --editable .
ENTRYPOINT ["uwsgi"]
CMD ["docker-uwsgi.ini"]
