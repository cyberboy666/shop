import os
import datetime

from chalice import Chalice
from chalice import Response

app = Chalice(app_name='shop_backend')

@app.route('/')
def index(pk=None):
    return Response(body='shop_backend')
