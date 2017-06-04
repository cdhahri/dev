#!/usr/bin/python3

import json
from datetime import datetime, timedelta

def process(r, target_path, w):
  try:
    with open(r, 'r') as file:
      tweets = json.load(file)
  except FileNotFoundError as e:
    print(e)
    return

  targets_file = open(target_path, 'r')

  out = {}
  for key in sorted(tweets.keys()):
    targets = targets_file.readline()
    targets = targets.rstrip().split('\t')
    if targets[0] == '-1':
      # Tue Sep 27 01:58:41 +0000 2016
      current_day = tweets[key]['created_at']
      current_day_object = datetime.strptime(current_day, '%a %b %d %H:%M:%S %z %Y')
      out['{0:%Y-%m-%d}'.format(current_day_object)] = None

  with open(w, 'w') as file:
    json.dump(out, file, sort_keys=True)


# main
with open('../ids/twitter.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = './raw/{}.json'.format(user_id)
  target_path = './tweet_text_per_line_result/{}_result.tsv'.format(user_id)
  w = './output/{}days.json'.format(user_id)
  process(r, target_path, w)
