FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN /opt/venv/bin/python3 -m pip install --upgrade pip

COPY requirements.txt /app/
EXPOSE 8000
RUN pip3 install --no-cache-dir -r requirements.txt &&\
    pip3 install --no-cache-dir mysqlclient
COPY . /app/