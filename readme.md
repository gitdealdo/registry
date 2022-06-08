# Registry System

## Installs for deploy on postgres
sudo apt install python3-dev postgresql postgresql-contrib python3-psycopg2 libpq-dev

## for developers

`git clone ...`

`cd backstore`

`virtualenv --python=python3 venv`

`pip install -r requirements/develop.txt`

`python manage.py makemigrations --settings=config.settings.develop account registry`

`python manage.py migrate --settings=config.settings.develop`

`python manage.py runserver --settings=config.settings.develop`

## for production

`git clone ...`

`cd backstore`

`virtualenv --python=python3 venv`

`pip install -r requirements.txt`

`./manage.py makemigrations --settings=config.settings.production account registry`

`./manage.py migrate --settings=config.settings.production`

`./manage.py createsuperuser --settings=config.settings.production`

`./manage.py runserver --settings=config.settings.production`

`./manage.py collectstatic --settings=config.settings.production`

#### for dump data

`python manage.py dumpdata account > fixtures/account.json --settings=config.settings.production`

`python manage.py dumpdata car > fixtures/car.json --settings=config.settings.production`

`python manage.py dumpdata control > fixtures/control.json --settings=config.settings.production`

#### for load data

`python manage.py loaddata fixtures/account.json --settings=config.settings.production`


