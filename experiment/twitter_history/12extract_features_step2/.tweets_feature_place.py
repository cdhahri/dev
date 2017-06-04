#!/usr/bin/python3

import api_foursquare

import config
token = config.load_token('/vagrant/config/foursquare.json')

r = '/vagrant/tmp/tweets.json'
w = '/vagrant/src/rf/data_tmp/pearson/place.json'

import json
with open(r, 'r') as file:
  tweets = json.load(file)

i = 0
categories = {}
feature = []
for tweet in tweets:
  key = 'None'
  if tweet['coordinates'] is not None:
    ll = tweet['coordinates']['coordinates']
    venue = api_foursquare.venue(token, ll[1], ll[0])
    if venue is not None and len(venue['categories']) > 0:
      print('{} * {}'.format(venue['name'].encode('utf-8'), venue['categories'][0]['name'].encode('utf-8')))
      key = venue['categories'][0]['name']
  if key not in categories:
    i += 1
    categories[key] = i
  feature.append(categories[key])

with open(w, 'w') as file:
  json.dump(feature, file)
