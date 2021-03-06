#!/bin/sh

if [ "$DATABASE" = "postgres" ]
  then
    echo "Waiting for psql"

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "Psql started"
fi

python manage.py flush --noinput
python manage.py migrate

exec "$@"