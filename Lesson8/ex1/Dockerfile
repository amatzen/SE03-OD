FROM ubuntu

RUN apt-get update && apt-get install -y build-essential
WORKDIR /project

COPY resources .

RUN make
