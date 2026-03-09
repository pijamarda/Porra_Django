#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

if [ "$DJANGO_LOADDATA" = "true" ]; then
  echo "Loading fixture data..."
  python manage.py loaddata euro2016

  echo "Creating superuser..."
  python manage.py createsuperuser --noinput || true

  echo "Creating test users..."
  echo "from django.contrib.auth.models import User; User.objects.get_or_create(username='zupo', defaults={'email':''})[0].set_password('password')" \
    | python manage.py shell || true
fi

echo "Starting gunicorn..."
exec gunicorn porrasite.wsgi:application --bind "0.0.0.0:${PORT:-8000}" --workers 2
