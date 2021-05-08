"""
    Messenger
    ----------
    Using twilio and PythonAnywhere it allows a user
    to set a timer on when a text message get sent.

    By (Kelvin) Chun Kit Cho
    May 8, 2021
"""

# Imports
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

# Global Variable
ACCOUNT_SID = os.environ.get('TWILIO_SID')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

# Creating a messenger class
class Messenger():
    def __init__(self) -> None:
        # Proxy server are require to be use for PythonAnyWhere
        self.proxy_client = TwilioHttpClient()
        self.proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        # Defining client
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN, http_client=self.proxy_client)

    # Text the message to a specific number
    def message(self, message, number):
        self.client.messages \
                    .create(
                        body="{}".format(message),
                        from_='+13472271948',
                        to=f'+1{number}'
                    )