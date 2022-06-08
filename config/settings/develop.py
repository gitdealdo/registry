from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

##########START_GRAPH_MODELS#########
INSTALLED_APPS += [
    'django_extensions',
]

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

# ./manage.py graph_models -a > fixtures/100122_model.dot --settings=config.settings.develop
# ./manage.py graph_models -a -g -o fixtures/100122_model.png --settings=config.settings.develop
##########END_GRAPH_MODELS#########

# For WS request
CORS_ORIGIN_WHITELIST = [
    'http://localhost:4200',
    'http://localhost:4300',
]


# CORS_ORIGIN_REGEX_WHITELIST = (
#     'htttp://localhost:7000',
# )
