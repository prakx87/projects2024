FROM python:3.11-slim-bullseye

RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY blog_site/ /blog_site/
WORKDIR /blog_site

COPY ./django_migrate.sh /django_migrate.sh
RUN chmod +x /django_migrate.sh

EXPOSE 8000

ENTRYPOINT ["/django_migrate.sh"]
