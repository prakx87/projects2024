FROM alpine:3.19.0

RUN apk update
RUN apk add postgresql14-client
RUN apk add bash

RUN echo "export PGPASSWORD=\${POSTGRES_PASSWORD}; psql -h postgres -U \${POSTGRES_USER} -d \${POSTGRES_DB}" > /usr/local/bin/psqlcli
RUN chmod +x /usr/local/bin/psqlcli

WORKDIR /dumps/

CMD ["/bin/bash", "-c", "while true; do sleep 60; done"]
