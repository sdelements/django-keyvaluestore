import os as _os

_PROJECT_PATH = _os.path.abspath(_os.path.dirname(__file__))

DEBUG = True
ADMINS = ()
MANAGERS = ADMINS
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "tests_db",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}
TIME_ZONE = "America/Chicago"
USE_TZ = True
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = True
USE_L10N = True

SECRET_KEY = "foobar"  # noqa: S105

MIDDLEWARE = ("django.middleware.common.CommonMiddleware",)

INSTALLED_APPS = ("keyvaluestore", "tests")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": True,
        },
    },
}
