#!/usr/bin/env python3

import requests

def geocode(address):
	parameters = {'address':address, 'sensor':'false'}
	base = 'http://maps.googleapis.com/maps/api/geocode/json'
	response = requests.get(base, params=parameters)
	answer = response.json()
	print(answer['results'][0]['geometry']['location'])

import http.client
import json
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'

def geocode2(address):
	path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
	print(quote_plus(address))
	connection = http.client.HTTPConnection('maps.google.com')
	connection.request('GET',path)
	rawreply = connection.getresponse().read()
	reply = json.loads(rawreply.decode('utf-8'))
	print(reply['results'][0]['geometry']['location'])


if __name__ == '__main__':
	geocode('16116 dawn marie lane, sugar land, tx')
	geocode2('16119 dawn marie lane, sugar land, TX')
