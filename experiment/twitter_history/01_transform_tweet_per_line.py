#!/usr/bin/python3

import json

with open('../ids/twitter.json', 'r') as file:
  ids = json.load(file)

ids = ['hoahoa']

for user_id in ids:
  try:
    with open('./raw/{}.json'.format(user_id), 'r') as file:
      tweets = json.load(file)
  except FileNotFoundError:
    print('FileNotFoundError - Skipping {}'.format(user_id))
    continue

  with open('./tweet_text_per_line/{}.csv'.format(user_id), 'w') as file:
    for tweet_id in sorted(tweets.keys()):
      file.write('{}\n'.format(tweets[tweet_id]['text'].replace('\r', ' ').replace('\n', ' ')))
