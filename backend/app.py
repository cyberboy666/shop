import os
import datetime

import stripe
from chalice import Chalice
from chalice import CORSConfig
from chalice import Response

app = Chalice(app_name='shop_backend')

stripe.api_key = 'sk_test_51Gw3HjJeAqoEzFKbQSRTfxXfV29Sa4daGkVF0hvKS8ofh5MfqbvClUlgfeq3kLaFkGO6vsCDNmcQMGlg351atbbd00XgifEU92'

cors_config = CORSConfig(
    allow_origin='*',
    # allow_headers=['X-Special-Header'],
    # max_age=600,
    # expose_headers=['X-Special-Header'],
    # allow_credentials=True
)

@app.route('/', cors=cors_config)
def index(pk=None):
    return Response(body='shop_backend')

@app.route('/create-checkout-session', methods=['POST'], cors=cors_config)
def create_checkout_session():
  session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'T-shirt',
        },
        'unit_amount': 2000,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='https://example.com/success',
    cancel_url='https://example.com/cancel',
  )

  return Response(body={"id": session.id})