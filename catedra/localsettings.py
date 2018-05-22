import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u+f(4=szno-!w(mk8@a=vwg&=4l-2^0b1(40)(iz2*3&u%khg6'