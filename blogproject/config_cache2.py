# encoding: utf-8
# from urllib.parse import urlparse
# import dj_database_url

# redis_url = urlparse(os.environ.get('REDISTOGO_URL', 'redis://localhost:6959'))
# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.cache.RedisCache',
#         'LOCATION': '{0}:{1}'.format(redis_url.hostname, redis_url.port),
#         'OPTIONS': {
#             'DB': 0,
#             'PASSWORD': redis_url.password,
#             'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
#             'PICKLE_VERSION': -1,  # Use the latest protocol version
#             'SOCKET_TIMEOUT': 60,  # in seconds
#             'IGNORE_EXCEPTIONS': True,
#         }
#     }
# }

CACHES = {
    'default': {
        # 'BACKEND': 'redis_cache.cache.RedisCache',
        "BACKEND": "django_redis.cache.RedisCache",
        'LOCATION': '127.0.0.1:6379',
        "OPTIONS": {
            "PASSWORD": "DhG7n&5q",
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            'PICKLE_VERSION': -1,  # Use the latest protocol version
            'SOCKET_TIMEOUT': 60,  # in seconds
            'IGNORE_EXCEPTIONS': True,
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        },
    },
}
REDIS_TIMEOUT=7*24*60*60
CUBES_REDIS_TIMEOUT=60*60
NEVER_REDIS_TIMEOUT=365*24*60*60

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# DJANGO_REDIS_IGNORE_EXCEPTIONS = True