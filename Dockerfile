#Dockerfile
FROM python:3.8-slim-buster
MAINTAINER Izek Chen

# Copy the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# Get source
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./app /app

# ENTRYPOINT [ "python" ]

CMD [ "python3", "-m" , "flask", "run"]