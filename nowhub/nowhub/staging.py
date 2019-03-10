# flake8: noqa
import os

from .base import *
from .firestore import FSClient

fs_client = FSClient()

DEBUG = True
ALLOWED_HOSTS = ['stagehub.appspot.com']

DATABASES = {}
