FROM mysql

ENV MYSQL_ALLOW_EMPTY_PASSWORD yes

COPY db-entrypoint/. /docker-entrypoint-initdb.d/ 
