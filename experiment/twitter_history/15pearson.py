#!/usr/bin/python3

import json
from scipy.stats import pearsonr
from scipy import stats

with open('../ids/twitter.json', 'r') as file:
  ids = json.load(file)

ids = ['hoahoa']

total = 0
total_hashtags_count = 0
total_mentions_count = 0
total_favourites_count = 0
total_media_count = 0
total_source = 0
total_week = 0
total_day_night = 0
total_active_passive = 0
total_mentions = 0
total_coordinates = 0
total_top_mentions = 0

hashtags_count_pearsons = []
mentions_count_pearsons = []
favourites_count_pearsons = []
media_count_pearsons = []
source_pearsons = []
week_pearsons = []
day_night_pearsons = []
active_passive_pearsons = []
mentions_pearsons = []
coordinates_pearsons = []
top_mentions_pearsons = []

for user_id in ids:
  r = './output/{}aggregated.json'.format(user_id)

  try:
    with open(r, 'r') as file:
      byday_aggregated = json.load(file)
  except FileNotFoundError as e:
    print(e)
    continue

  target = []
  hashtags_count = []      
  mentions_count = []
  favourites_count = []
  media_count = []
  source = []
  week = []
  day_night = []
  active_passive = []
  mentions = []
  coordinates = []
  top_mentions = []

  for key in sorted(byday_aggregated.keys()):
    target.append(byday_aggregated[key]['_target'])
    hashtags_count.append(byday_aggregated[key]['hashtags_count'])
    mentions_count.append(byday_aggregated[key]['mentions_count'])
    favourites_count.append(byday_aggregated[key]['favourites_count'])
    media_count.append(byday_aggregated[key]['media_count'])
    source.append(byday_aggregated[key]['source'])
    week.append(byday_aggregated[key]['week'])
    day_night.append(byday_aggregated[key]['day_night'])
    active_passive.append(byday_aggregated[key]['active_passive'])
    mentions.append(byday_aggregated[key]['mentions'])
    coordinates.append(byday_aggregated[key]['coordinates'])
    top_mentions.append(byday_aggregated[key]['top_mentions'])

  if len(set(target)) < 2:
    continue

  total += 1

#  target = stats.zscore(target).tolist()

#  '''
  hashtags_count = stats.zscore(hashtags_count).tolist()
  hashtags_count_pearson = pearsonr(target, hashtags_count)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(hashtags_count_pearson[0]) > percentage and abs(hashtags_count_pearson[1]) < 0.05:
      hashtags_count_pearsons.append(abs(hashtags_count_pearson[0]))
#      total_hashtags_count += 1
#      print(percentage)
      print(user_id)
    print('@{}'.format(hashtags_count_pearson[0]))
    print('@{}'.format(hashtags_count_pearson[1]))
#  '''

#  '''
  mentions_count = stats.zscore(mentions_count).tolist()
  mentions_count_pearson = pearsonr(target, mentions_count)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(mentions_count_pearson[0]) > percentage and abs(mentions_count_pearson[1]) < 0.05:
      mentions_count_pearsons.append(abs(mentions_count_pearson[0]))
#      total_mentions_count += 1
#      print(percentage)
      print(user_id)
    print('@{}'.format(mentions_count_pearson[0]))
    print('@{}'.format(mentions_count_pearson[1]))
#  '''

#  '''
  favourites_count = stats.zscore(favourites_count).tolist()
  favourites_count_pearson = pearsonr(target, favourites_count)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(favourites_count_pearson[0]) > percentage and abs(favourites_count_pearson[1]) < 0.05:
      favourites_count_pearsons.append(abs(favourites_count_pearson[0]))
#      total_favourites_count += 1
#      print(percentage)
      print(user_id)
    print('@{}'.format(favourites_count_pearson[0]))
    print('@{}'.format(favourites_count_pearson[1]))
#  '''

#  '''
  media_count = stats.zscore(media_count).tolist()
  media_count_pearson = pearsonr(target, media_count)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(media_count_pearson[0]) > percentage and abs(media_count_pearson[1]) < 0.05:
      media_count_pearsons.append(abs(media_count_pearson[0]))
#      total_media_count += 1
#      print(percentage)
      print(user_id)
    print('@{}'.format(media_count_pearson[0]))
    print('@{}'.format(media_count_pearson[1]))
#  '''

  '''
  # print(source)
  # if len(set(source)) < 2:
  #   continue
  source = stats.zscore(source).tolist()
  source_pearson = pearsonr(target, source)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(source_pearson[0]) > percentage and abs(source_pearson[1]) < 0.05:
      source_pearsons.append(abs(source_pearson[0]))
#      total_source += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(source_pearson[0]))
#    print('@{}'.format(source_pearson[1]))
  '''

#  '''
  week = stats.zscore(week).tolist()
  week_pearson = pearsonr(target, week)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(week_pearson[0]) > percentage and abs(week_pearson[1]) < 0.05:
      week_pearsons.append(abs(week_pearson[0]))
#      total_week += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(week_pearson[0]))
#    print('@{}'.format(week_pearson[1]))
#  '''

#  '''
  if len(set(day_night)) < 2:
    continue
  day_night = stats.zscore(day_night).tolist()
  day_night_pearson = pearsonr(target, day_night)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(day_night_pearson[0]) > percentage and abs(day_night_pearson[1]) < 0.05:
      day_night_pearsons.append(abs(day_night_pearson[0]))
#      total_day_night += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(active_passive_pearson[0]))
#    print('@{}'.format(active_passive_pearson[1]))
#  '''

#  '''
  if len(set(active_passive)) < 2:
    continue
  active_passive = stats.zscore(active_passive).tolist()
  active_passive_pearson = pearsonr(target, active_passive)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(active_passive_pearson[0]) > percentage and abs(active_passive_pearson[1]) < 0.05:
      active_passive_pearsons.append(abs(active_passive_pearson[0]))
#      total_active_passive += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(active_passive_pearson[0]))
#    print('@{}'.format(active_passive_pearson[1]))
#  '''

#  '''
  target_mentions = []
  mentions_mentions = []
  for i in range(len(target)):
    for j in range(len(mentions[i])):
      #?
      #if mentions[i][j] == -100:
      #  continue
      target_mentions.append(target[i])
      mentions_mentions.append(mentions[i][j])
  if len(set(mentions_mentions)) < 2:
    continue
  mentions_mentions = stats.zscore(mentions_mentions).tolist()
  mentions_pearson = pearsonr(target_mentions, mentions_mentions)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(mentions_pearson[0]) > percentage and abs(mentions_pearson[1]) < 0.05:
      mentions_pearsons.append(abs(mentions_pearson[0]))
#      total_mentions += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(mentions_pearson[0]))
#    print('@{}'.format(mentions_pearson[1]))
#  '''

#  '''
  target_coordinates = []
  coordinates_coordinates = []
  for i in range(len(target)):
    for j in range(len(coordinates[i])):
      if coordinates[i][j] == -100:
        continue
      target_coordinates.append(target[i])
      coordinates_coordinates.append(coordinates[i][j])
  if len(set(coordinates_coordinates)) < 2:
    continue
  coordinates_coordinates = stats.zscore(coordinates_coordinates).tolist()
  coordinates_pearson = pearsonr(target_coordinates, coordinates_coordinates)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(coordinates_pearson[0]) > percentage and abs(coordinates_pearson[1]) < 0.05:
      coordinates_pearsons.append(abs(coordinates_pearson[0]))
#      total_coordinates += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(coordinates_pearson[0]))
#    print('@{}'.format(coordinates_pearson[1]))
#  '''

#  '''
  target_top_mentions = []
  top_mentions_mentions = []
  for i in range(len(target)):
    for j in range(len(top_mentions[i])):
      #?
      #if top_mentions[i][j] == -100:
      #  continue
      target_top_mentions.append(target[i])
      top_mentions_mentions.append(top_mentions[i][j])
  if len(set(top_mentions_mentions)) < 2:
    continue
  top_mentions_mentions = stats.zscore(top_mentions_mentions).tolist()
  top_mentions_pearson = pearsonr(target_top_mentions, top_mentions_mentions)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(top_mentions_pearson[0]) > percentage and abs(top_mentions_pearson[1]) < 0.05:
      top_mentions_pearsons.append(abs(top_mentions_pearson[0]))
#      total_top_mentions += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(top_mentions_pearson[0]))
#    print('@{}'.format(top_mentions_pearson[1]))
#  '''




  '''
  count_all_capital = stats.zscore(count_all_capital).tolist()
  count_all_capital_pearson = pearsonr(target, count_all_capital)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(count_all_capital_pearson[0]) > percentage and abs(count_all_capital_pearson[1]) < 0.05:
#      count_all_capital_pearsons.append(abs(count_all_capital_pearson[0]))
#      total_hashtags_count += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(hashtags_count_pearson[0]))
#    print('@{}'.format(hashtags_count_pearson[1]))
  '''

  '''
  count_exclamation_mark = stats.zscore(count_exclamation_mark).tolist()
  count_exclamation_mark_pearson = pearsonr(target, count_exclamation_mark)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(count_exclamation_mark_pearson[0]) > percentage and abs(count_exclamation_mark_pearson[1]) < 0.05:
#      count_all_capital_pearsons.append(abs(count_all_capital_pearson[0]))
#      total_hashtags_count += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(hashtags_count_pearson[0]))
#    print('@{}'.format(hashtags_count_pearson[1]))
  '''

  '''
  count_question_mark = stats.zscore(count_question_mark).tolist()
  count_question_mark_pearson = pearsonr(target, count_question_mark)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(count_question_mark_pearson[0]) > percentage and abs(count_question_mark_pearson[1]) < 0.05:
#      count_all_capital_pearsons.append(abs(count_all_capital_pearson[0]))
#      total_hashtags_count += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(hashtags_count_pearson[0]))
#    print('@{}'.format(hashtags_count_pearson[1]))
  '''

  '''
  count_negative_word = stats.zscore(count_negative_word).tolist()
  count_negative_word_pearson = pearsonr(target, count_negative_word)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(count_negative_word_pearson[0]) > percentage and abs(count_negative_word_pearson[1]) < 0.05:
#      count_all_capital_pearsons.append(abs(count_all_capital_pearson[0]))
#      total_hashtags_count += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(hashtags_count_pearson[0]))
#    print('@{}'.format(hashtags_count_pearson[1]))
  '''

  '''
  count_positive_word = stats.zscore(count_positive_word).tolist()
  count_positive_word_pearson = pearsonr(target, count_positive_word)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(count_positive_word_pearson[0]) > percentage and abs(count_positive_word_pearson[1]) < 0.05:
#      count_all_capital_pearsons.append(abs(count_all_capital_pearson[0]))
#      total_hashtags_count += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(hashtags_count_pearson[0]))
#    print('@{}'.format(hashtags_count_pearson[1]))
  '''

  '''
  exist_more_than_three_dots = stats.zscore(exist_more_than_three_dots).tolist()
  exist_more_than_three_dots_pearson = pearsonr(target, exist_more_than_three_dots)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(exist_more_than_three_dots_pearson[0]) > percentage and abs(exist_more_than_three_dots_pearson[1]) < 0.05:
#      count_all_capital_pearsons.append(abs(count_all_capital_pearson[0]))
#      total_hashtags_count += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(hashtags_count_pearson[0]))
#    print('@{}'.format(hashtags_count_pearson[1]))
  #'''

  '''
  exist_more_than_three_vowels = stats.zscore(exist_more_than_three_vowels).tolist()
  exist_more_than_three_vowels_pearson = pearsonr(target, exist_more_than_three_vowels)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(exist_more_than_three_vowels_pearson[0]) > percentage and abs(exist_more_than_three_vowels_pearson[1]) < 0.05:
#      count_all_capital_pearsons.append(abs(count_all_capital_pearson[0]))
#      total_hashtags_count += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(hashtags_count_pearson[0]))
#    print('@{}'.format(hashtags_count_pearson[1]))
  '''

'''
print('{}'.format(total_hashtags_count/total))
print('{}'.format(total_mentions_count/total))
print('{}'.format(total_favourites_count/total))
print('{}'.format(total_media_count/total))
print('{}'.format(total_source/total))
print('{}'.format(total_week/total))
print('{}'.format(total_day_night/total))
print('{}'.format(total_active_passive/total))
print('{}'.format(total_mentions/total))
print('{}'.format(total_coordinates/total))
print('{}'.format(total_top_mentions/total))
'''

'''
import numpy as np

a = np.array([hashtags_count_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([mentions_count_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([favourites_count_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([media_count_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([source_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([week_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([day_night_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([active_passive_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([mentions_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([coordinates_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
'''
