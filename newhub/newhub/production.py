# flake8: noqa
import os

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['newhub.space']
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']


DATABASES = {
}
