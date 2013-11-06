from .base import *  # noqa


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'docs',
        'USER': 'postgres',  # Not used with sqlite3.
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = False
TEMPLATE_DEBUG = False
CELERY_ALWAYS_EAGER = False

MEDIA_URL = 'https://uedocs01.csgicorp.com/'
STATIC_URL = 'https://uedocs01.csgicorp.com/static/'
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://odin:8983/solr',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
        'PREFIX': 'docs',
        'OPTIONS': {
            'DB': 1,
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        },
    },
}

# Elasticsearch settings.
ES_HOSTS = ['backup:9200', 'db:9200']
ES_DEFAULT_NUM_REPLICAS = 1
ES_DEFAULT_NUM_SHARDS = 5

SLUMBER_API_HOST = 'https://uedocs01.csgicorp.com'
WEBSOCKET_HOST = 'uedocs01.csgicorp.com:8088'

PRODUCTION_DOMAIN = 'uedocs01.csgicorp.com'
USE_SUBDOMAIN = True
NGINX_X_ACCEL_REDIRECT = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")


try:
    from local_settings import *  # noqa
except:
    pass
