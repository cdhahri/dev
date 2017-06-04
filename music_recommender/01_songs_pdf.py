#!/usr/bin/python3

def count_songs(songs, mood, songs_pdf):
  for song in songs[mood]:
    if song not in songs_pdf:
      songs_pdf[song] = {'-':0,'~':0,'+':0,'*':0}
    songs_pdf[song]['*'] += 1
    songs_pdf[song][mood] += 1

songs_pdf = {}

def max_probability(songs_pdf, mood):
  max_so_far = 0
  for song in songs_pdf.values():
    if song[mood] > max_so_far:
      max_so_far = song[mood]
  return max_so_far

import json
with open('./data/songs_per_mood_per_user_filtered.json', 'r') as file:
  songs_per_mood_per_user = json.load(file)

for user_songs in songs_per_mood_per_user.values():
  count_songs(user_songs, '-', songs_pdf)
  count_songs(user_songs, '~', songs_pdf)
  count_songs(user_songs, '+', songs_pdf)

total = 0
total_negative = 0
total_neutral = 0
total_positive = 0

for song in songs_pdf.values():
  total += song['*']
  total_negative += song['-']
  total_neutral += song['~']
  total_positive += song['+']

for song, pdf in songs_pdf.items():
  pdf['*'] /= total
  pdf['-'] /= total_negative
  pdf['~'] /= total_neutral
  pdf['+'] /= total_positive

with open('./data/songs_pdf.json', 'w') as file:
  json.dump(songs_pdf, file, sort_keys=True)

print(len(songs_pdf.keys()))

with open('./data/songs_selected.json', 'r') as file:
  songs_selected = json.load(file)

for id_user, songs in songs_selected.items():
  for mood, song in songs.items():
    pdf = songs_pdf[song[0]]

#    if pdf[mood] > pdf['*']:
#      print('1')
#    else:
#      print('-1')

#    max_ = max_probability(songs_pdf, mood)
#    if pdf[mood] >= max_:
#      print('2')      
#    else:
#      print('-2')

