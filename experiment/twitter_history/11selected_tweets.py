#!/usr/bin/python3

sources = {
  '<a href="http://foursquare.com" rel="nofollow">Foursquare</a>':None,
  '<a href="http://instagram.com" rel="nofollow">Instagram</a>':None
}

import json
from datetime import datetime, timedelta
        
def process(tweets, selected_days, targets_file, w):
  out = {}
  for key in sorted(tweets.keys()):
    targets = targets_file.readline()
    targets = targets.rstrip().split('\t')
    # Tue Sep 27 01:58:41 +0000 2016
    # if targets[0] == '0':
    # if tweets[key]['source'] not in sources or targets[i] != '0':
      # continue
    current_day = tweets[key]['created_at']
    current_day_object = datetime.strptime(current_day, '%a %b %d %H:%M:%S %z %Y')
    next_day_object = current_day_object + timedelta(days=1)
    if '{0:%Y-%m-%d}'.format(next_day_object) in selected_days:# and tweets[key]['source'] in sources:
      out[key] = tweets[key]

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
  with open(selected_days_path, 'r') as file:
    selected_days = json.load(file)
  targets_file = open(target_path, 'r')

  for percentage in percentages:
    length = int((percentage/10)*(len(selected_days.keys())))
    selected_days_subset = {}
    i = -1
    for key in sorted(selected_days.keys()):
      i += 1
      if i == length:
        break
      selected_days_subset[key] = selected_days[key]

    w = './output/{}tweets_selected.json'.format(user_id)
    process(tweets, selected_days_subset, targets_file, w)
