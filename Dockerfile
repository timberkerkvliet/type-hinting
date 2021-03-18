FROM python:3.8

WORKDIR /

ADD requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt