#!/usr/bin/python3

percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentages = [10]

import json
import os.path

# users
with open('../ids/twitter.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  for percentage in percentages:
    r = './output/{}features_step3.json'.format(user_id)
    w = './output/{}aggregated.json'.format(user_id)

    try:
      with open(r, 'r') as file:
        byday = json.load(file)
    except FileNotFoundError as e:
      print(e)
      continue

    i = 0
    auto_inc = {}
    k = 0
    auto_inc_mentions = {}
    l = 0
    auto_inc_top_mentions = {}
    byday_aggregated = {}
    for key, day in byday.items():
      target = day['_target']
      pos = target.count('1')
      neg = target.count('-1')
      #neu = target.count('0')
      try:
        target = (pos) / (pos + neg)
      except ZeroDivisionError:
        print('divide by 0')
        continue

#     target_current = day['_target_current']
#     pos = target_current.count('4')
#     neg = target_current.count('0')
#     target_current = pos / (pos + neg)

      hashtags_count = day['hashtags_count']
      hashtags_count = sum(hashtags_count)

      mentions_count = day['mentions_count']
      mentions_count = sum(mentions_count)

      favourites_count = day['favourites_count']
      favourites_count = sum(favourites_count)

      media_count = day['media_count']
      media_count = sum(media_count)

      j = 0
      auto_inc2 = {}
      source = day['source']
      source_values = []
      for sss in source:
        if sss not in auto_inc2:
          j += 1
          auto_inc2[sss] = j
        source_values.append(auto_inc2[sss])

      source_twitter_or_not = day['source_twitter_or_not']
      source_twitter_or_not = sum(source_twitter_or_not)

      try:
        week = day['week'][0]
      except IndexError:
        continue

      day_night = day['day_night']
      d = 0
      n = 0
      for dn in day_night:
        if int(dn) > 20 or int(dn) < 6:
          n += 1
        else:
          d += 1
      day_night = d / (d + n)

      active_passive = day['active_passive']
      pos = active_passive.count(1)
      neg = active_passive.count(-1)
      active_passive = pos / (pos + neg)

      mentions = day['mentions']
      mentions_values = []
      for mention in mentions:
        if mention not in auto_inc_mentions:
          k += 1
          auto_inc_mentions[mention] = k
        mentions_values.append(auto_inc_mentions[mention])

      top_mentions = day['top_mentions']
      top_mentions_values = []
      for mention in top_mentions:
        if mention not in auto_inc_top_mentions:
          l += 1
          auto_inc_top_mentions[mention] = l
        top_mentions_values.append(auto_inc_top_mentions[mention])

      '''
      mentions = day['mentions']
      moods = []
      for mention in mentions:
        if not os.path.exists('/vagrant/data/osn-data/features_step3/mentions/past_tweets/aggregated/{}.json'.format(mention)):
          continue
        with open('/vagrant/data/osn-data/features_step3/mentions/past_tweets/aggregated/{}.json'.format(mention), 'r') as file:
          mention_history = json.load(file)
        if key in mention_history:
          moods.append(mention_history[key]['_target'])
      #
      if len(moods) == 0:
        moods = [0]
      import numpy
      moods = numpy.mean(moods)
      '''

      '''
      tags = day['tags']
      tags_values = []
      for tag in tags:
        if tag not in auto_inc:
          i += 1
          auto_inc[tag] = i
        tags_values.append(auto_inc[tag])
      '''

      j = 0
      auto_inc2 = {}
      coordinates = day['coordinates']
      coordinates_values = []
      for coordinate in coordinates:
        if coordinate is None:
          coordinates_values.append(-100)
          continue
        if coordinate not in auto_inc2:
          j += 1
          auto_inc2[coordinate] = j
        coordinates_values.append(auto_inc2[coordinate])

      byday_aggregated[key] = {
        '_target':target,
  #      '_target_current':target_current,
        'hashtags_count':hashtags_count,
        'mentions_count':mentions_count,
        'favourites_count':favourites_count,
        'media_count':media_count,
        'source':source_values,
        'source_twitter_or_not':source_twitter_or_not,
        'week':week,
        'day_night':day_night,
        'active_passive':active_passive,
        'mentions':mentions_values,
  #      'tags':tags_values,
        'coordinates':coordinates_values,
        'top_mentions':top_mentions_values,
      }

    with open(w, 'w') as file:
      json.dump(byday_aggregated, file, sort_keys=True)
