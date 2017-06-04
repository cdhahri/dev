#!/usr/bin/python3

import json
from datetime import datetime, timedelta
        
def process(tweets, targets_file, selected_days, w):
  out = {}
  for key in sorted(tweets.keys()):
    targets = targets_file.readline()
    targets = targets.rstrip().split('\t')
    if targets[0] == '0':
      continue
    # Tue Sep 27 01:58:41 +0000 2016
    current_day = tweets[key]['created_at']
    current_day_object = datetime.strptime(current_day, '%a %b %d %H:%M:%S %z %Y')
    current_day = '{0:%Y-%m-%d}'.format(current_day_object)
    if current_day in selected_days:
      if current_day not in out:
        out[current_day] = []
      out[current_day].append(targets[0])

  with open(w, 'w') as file:
    json.dump(out, file, sort_keys=True)


# main
with open('../ids/twitter.json', 'r') as file:
  ids = json.load(file)

percentages = [10]

for user_id in ids:
  r = './raw/{}.json'.format(user_id)
  target_path = './tweet_text_per_line_result/{}_result.tsv'.format(user_id)
  selected_days_path = './output/{}days.json'.format(user_id)

  try:
    with open(r, 'r') as file:
      tweets = json.load(file)
  except FileNotFoundError as e:
    print(e)
    continue
  targets_file = open(target_path, 'r')
  with open(selected_days_path, 'r') as file:
    selected_days = json.load(file)

  for percentage in percentages:
    length = int((percentage/10)*(len(selected_days.keys())))
    selected_days_subset = {}
    i = -1
    for key in sorted(selected_days.keys()):
      i += 1
      if i == length:
        break
      selected_days_subset[key] = selected_days[key]

    w = './output/{}target.json'.format(user_id)
    process(tweets, targets_file, selected_days_subset, w)
