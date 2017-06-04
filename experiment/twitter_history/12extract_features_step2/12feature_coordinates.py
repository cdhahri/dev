#!/usr/bin/python3

percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentages = [10]

import json

with open('../../ids/twitter.json', 'r') as file:
  ids = json.load(file)

# categories
#with open('/vagrant/data/osn-data/category_coordinates_grouped.json', 'r') as file:
#  category_coordinates = json.load(file)

for user_id in ids:
  for percentage in percentages:
    r = '../output/{}tweets_selected.json'.format(user_id)
    w = '../output/{}coordinates.json'.format(user_id)

    try:
      with open(r, 'r') as file:
        tweets_hash = json.load(file)
    except FileNotFoundError as e:
      print(e)
      continue

    tweets = []
    for key in sorted(tweets_hash.keys()):
      tweets.append(tweets_hash[key])

    feature = []
    for tweet in tweets:
      if tweet['coordinates'] is None:
        feature.append(None)
        continue
      ll = tweet['coordinates']['coordinates']
      ll_string = json.dumps(ll, sort_keys=True)
      '''
      #print('{}: processing...'.format(ll_string))
      category = None
      if ll_string in category_coordinates:
        category = category_coordinates[ll_string]
      feature.append(category)
      '''
      feature.append(ll_string)

    with open(w, 'w') as file:
      json.dump(feature, file)
