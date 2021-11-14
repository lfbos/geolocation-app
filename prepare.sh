#!/bin/sh

until PGPASSWORD=$POSTGRES_PASSWORD psql -h $POSTGRES_HOST -U $POSTGRES_USER -c '\q'; do
  echo "Waiting for postgres server"
  sleep 1
done

# Load migrations
python manage.py migrate --noinput

# Load fixtures
python manage.py loaddata languages.json
python manage.py loaddata currencies.json

# Create superuser
python manage.py createadmin --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL --password $DJANGO_SUPERUSER_PASSWORD

# Collect static files
python manage.py collectstatic --no-input

exec "$@"