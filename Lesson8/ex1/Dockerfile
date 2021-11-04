FROM ubuntu

RUN apt-get update && apt-get install -y build-essential

COPY . .

CMD ["gcc", "*.c", "-o", "o"]
