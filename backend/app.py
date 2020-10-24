import os
import datetime
import sentry_sdk

from chalice import Chalice
from chalice import Response

app = Chalice(app_name='shop_backend')

@app.route('/')
def index(pk=None):
    return Response(body='{{cookiecutter.app_name}}')
