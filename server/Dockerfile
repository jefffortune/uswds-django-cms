FROM python:3.11
WORKDIR /app
COPY app /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt
CMD uwsgi --http=0.0.0.0:80 --module=core.wsgi
