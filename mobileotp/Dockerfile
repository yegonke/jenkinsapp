FROM python:3.8.5-alpine

# Create app directory
WORKDIR /app/mobileotp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev postgis gcc python3-dev musl-dev geos gdal \
    && apk add jpeg-dev zlib-dev libjpeg

# Install app dependencies
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Bundle app source
# RUN rm -r -f static
COPY . .

COPY entrypoint.sh ./
ENTRYPOINT ["sh", "entrypoint.sh"]
