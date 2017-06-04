#!/usr/bin/python3

sources = {
  '<a href="http://runkeeper.com" rel="nofollow">Runkeeper</a>':None,
}

percentages = [10]

import json

with open('../ids2.json', 'r') as file:
  ids = json.load(file)

# for user_id in ids:
#   for percentage in percentages:
#     r = '../tweets_selected/{}/{}.json'.format(percentage, user_id)
#     w = '../tweets_selected/features_step2/{}/{}source_runkeeper_or_not.json'.format(percentage, user_id)

#     with open(r, 'r') as file:
#       tweets_hash = json.load(file)

#     tweets = []
#     for key in sorted(tweets_hash.keys()):
#       tweets.append(tweets_hash[key])

#     feature = []
#     for tweet in tweets:
#       if tweet['source'] in sources:
#         feature.append(1)
#       else:
#         feature.append(0)

#     with open(w, 'w') as file:
#       json.dump(feature, file)

import re
regex = '^Just completed a (.+) (km|mi) (.+) with @?#?Runkeeper\. .+$'

for user_id in ids:
  for percentage in percentages:
    r = '../tweets_selected/{}/{}.json'.format(percentage, user_id)
    w1 = '../tweets_selected/features_step2/{}/{}runkeeper_distance.json'.format(percentage, user_id)
    w2 = '../tweets_selected/features_step2/{}/{}runkeeper_activity.json'.format(percentage, user_id)

    with open(r, 'r') as file:
      tweets_hash = json.load(file)

    tweets = []
    for key in sorted(tweets_hash.keys()):
      tweets.append(tweets_hash[key])

    feature1 = []
    feature2 = []
    for tweet in tweets:
      if tweet['source'] not in sources:
        feature1.append(-1.0)
        feature2.append('NO')
      m = re.match(regex, tweet['text'])
      if m is not None:
        distance = float(m.group(1))
        if m.group(2) == 'mi':
          distance = distance * 1.60934
        activity = m.group(3)
        feature1.append(distance)
        feature2.append(activity)
      else:
        feature1.append(-1.0)
        feature2.append('NO')

    with open(w1, 'w') as file:
      json.dump(feature1, file)
    with open(w2, 'w') as file:
      json.dump(feature2, file)
