FROM python:3.10

WORKDIR /opt/app

ENV DJANGO_SETTINGS_MODULE 'company.settings'
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240


COPY requirements.txt requirements.txt
#COPY uwsgi/uwsgi.ini uwsgi.ini

RUN  mkdir -p /var/www/static/ \
     && mkdir -p /opt/app/static/ \
     && mkdir -p /var/www/logs/ \
     && pip install --upgrade pip --no-cache-dir \
     && pip install -r requirements.txt --no-cache-dir

COPY . .

ENV PYTHONPATH ${PYTHONPATH}:/opt/app/company

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]