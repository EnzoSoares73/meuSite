FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
EXPOSE 8000
RUN pip3 install -r requirements.txt
RUN pip3 install mysqlclient
COPY . /app/