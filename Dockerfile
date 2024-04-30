# syntax=docker/dockerfile:1

FROM python:3.11.4-alpine

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8080

ENTRYPOINT ["python3"]
CMD ["-m" , "flask", "run", "--host=0.0.0.0"]
