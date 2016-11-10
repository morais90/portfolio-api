from .production import *  # noqa

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa
    }
}

MIDDLEWARE_CLASSES.append('cargobr_api.extra.middlewares.CorsMiddleware');  # noqa
