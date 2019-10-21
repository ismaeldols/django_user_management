#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate --noinput
python manage.py collectstatic --no-input --clear

python manage.py createsuperuserwithpassword --username test --iban IL952197497867939996202 --first_name test --last_name test --email test@test.com --password test --preserve
# Add assignment for user@gmail.com >  match username=user domain=gmail.com, weight=100, user=test  ## TODO: ADD MANAGE.PY COMMAND TO ADD IT

exec "$@"