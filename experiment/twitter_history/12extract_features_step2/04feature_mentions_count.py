#!/usr/bin/python3

percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentages = [10]

import json

with open('../../ids/twitter.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  for percentage in percentages:
    r = '../output/{}tweets_selected.json'.format(user_id)
    w = '../output/{}mentions_count.json'.format(user_id)

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
      count = len(tweet['entities']['user_mentions'])
      feature.append(count)

    with open(w, 'w') as file:
      json.dump(feature, file)
