import requests
import json
import unittest
from unittest import mock
from credentials import token


class RegistrantClass:
    def fetch_registrant(self, url):
        response = requests.get(url, headers={'Authorization': 'Bearer ' + token})
        registrants = response.json()

        return str(len(registrants['registrants']))
