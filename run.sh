#!/bin/sh

until PGPASSWORD=$POSTGRES_PASSWORD psql -h $POSTGRES_HOST -U $POSTGRES_USER -d $POSTGRES_DB -c '\q'; do
  echo "Waiting for postgres server"
  sleep 1
done

if [ "$DEBUG" = "True" ]
  then
      echo "WITH RELOAD"
      gunicorn geolocation.wsgi:application --workers=4 --log-file=- --log-level=info --bind 0.0.0.0:8080 --reload
  else
      echo "without reload"
      gunicorn geolocation.wsgi:application --workers=4 --log-file=- --log-level=info --bind 0.0.0.0:8080
fi

exec "$@"