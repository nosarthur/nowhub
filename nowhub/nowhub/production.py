# flake8: noqa
import os

from .base import *
from .firestore import FSClient

fs_client = FSClient()

DEBUG = False
ALLOWED_HOSTS = ['nowhub.space', 'nowhub.appspot.com']
SECRET_KEY = fs_client.get('secret_key')

DATABASES = {}
