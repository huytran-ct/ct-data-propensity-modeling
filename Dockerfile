FROM python:3.7

WORKDIR /opt
COPY requirements.txt /opt
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
COPY . /opt
EXPOSE 8080
RUN python main.py