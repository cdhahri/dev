#!/usr/bin/python3

percentages = [10]

days = {
  'Mon': 1,
  'Tue': 1,
  'Wed': 1,
  'Thu': 1,
  'Fri': 1,
  'Sat': 2,
  'Sun': 2,
}

import json

with open('../../ids/twitter.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  for percentage in percentages:
    r = '../output/{}tweets_selected.json'.format(user_id)
    w = '../output/{}week.json'.format(user_id)

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
    day = tweet['created_at'][:3]
    feature.append(days[day])

  with open(w, 'w') as file:
    json.dump(feature, file)
