FROM python:3.9.0-alpine

# set work directory
WORKDIR /usr/src/chat_ws

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create the app user
RUN addgroup -S app && adduser -S app -G app --home /usr/src/chat_ws

# install psycopg2 dependencies
RUN apk update \
    && apk add gcc musl-dev libffi-dev openssl-dev python3-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# chown all the files to the app user
RUN chown -R app:app .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]