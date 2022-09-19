FROM python:3.9

WORKDIR /opt
COPY requirements.txt /opt
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
COPY . /opt
EXPOSE 8080
CMD exec gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 --timeout 0 main:app