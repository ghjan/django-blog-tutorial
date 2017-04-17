DEBUG = True

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '192.168.4.154:6379:3',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
            # 'PASSWORD': 'secretpassword',
            'PICKLE_VERSION': -1,  # Use the latest protocol version
            'SOCKET_TIMEOUT': 60,  # in seconds
            'IGNORE_EXCEPTIONS': True,
        }
    }
}
