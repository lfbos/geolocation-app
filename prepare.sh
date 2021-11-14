#!/bin/sh

until PGPASSWORD=$POSTGRES_PASSWORD psql -h $POSTGRES_HOST -U $POSTGRES_USER -c '\q'; do
  echo "Waiting for postgres server"
  sleep 1
done

# Load migrations
python manage.py migrate --noinput
# Collect static files
python manage.py collectstatic --no-input
# Load fixtures
# python manage.py load_fixtures --file=apps/accounts/fixtures/groups.json

exec "$@"