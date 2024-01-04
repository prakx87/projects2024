FROM prakx/djangoblog:v1

RUN apt-get update
RUN apt-get install wget gnupg -y

RUN bash -c 'echo "deb https://apt.postgresql.org/pub/repos/apt focal-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get update
RUN apt-get install postgresql-client-14 -y

RUN echo "export PGPASSWORD=\${DB_PASS}; psql -h \${DB_HOST} -U \${DB_USER} -d \${DB_NAME}" > /usr/local/bin/psqlcli
RUN chmod +x /usr/local/bin/psqlcli

RUN useradd -ms /bin/bash localuser

RUN chown -R localuser:localuser /blog_site
RUN mkdir /dumps/
RUN chown -R localuser:localuser /dumps

WORKDIR /dumps/

USER localuser

ENTRYPOINT [""]

CMD ["/bin/bash", "-c", "while true; do sleep 60; done"]
