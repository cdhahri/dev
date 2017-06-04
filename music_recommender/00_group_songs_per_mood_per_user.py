#!/usr/bin/python3

def load_song_entries_for_mood(mood):
  try:
    return open('./sample_LJ2M/info/{}.csv'.format(mood), 'r')
  except FileNotFoundError as e:
    if str(e) == '[Errno 2] No such file or directory: \'./sample_LJ2M/info/{}.csv\''.format(mood):
      print('Skipping {}'.format(mood))
      return []
    else:
      raise Exception('#1')

def filter_users_with_few_songs(songs_per_mood_per_user):
  songs_per_mood_per_user_filtered = {}

  for id_user, songs in songs_per_mood_per_user.items():
    valid = True
    for songs_per_category in songs.values():
      if len(songs_per_category) <= 1:
        valid = False
        break
    if valid:
      songs_per_mood_per_user_filtered[id_user] = songs

  return songs_per_mood_per_user_filtered

songs_per_mood_per_user = {}

import json
with open('./data/mood_category.json', 'r') as file:
  mood_to_category_hash = json.load(file)

for mood in sorted(mood_to_category_hash.keys()):
  mood_category = mood_to_category_hash[mood] # -, ~ or +

  song_entries = load_song_entries_for_mood(mood)

  for song_entry in song_entries:
    song_entry_columns = song_entry.rstrip().split(',')

    # accomplished_5,u402076,All Along the Watchtower - Jimi Hendrix,Jimi Hendrix,All Along The Watchtower,7450753,TRWMZOQ12903CC16CB
    id_user = song_entry_columns[1]
    #id_echonest = song_entry_columns[-1]
    id_7digital = song_entry_columns[-2]

    if id_7digital not in [None, '']:
      if id_user not in songs_per_mood_per_user:
        songs_per_mood_per_user[id_user] = {'-':[],'~':[],'+':[]}
      songs_per_mood_per_user[id_user][mood_category].append(id_7digital)

with open('./data/songs_per_mood_per_user.json', 'w') as file:
  json.dump(songs_per_mood_per_user, file, sort_keys=True)

songs_per_mood_per_user_filtered = filter_users_with_few_songs(songs_per_mood_per_user)

with open('./data/songs_per_mood_per_user_filtered.json', 'w') as file:
  json.dump(songs_per_mood_per_user_filtered, file, sort_keys=True)

songs_selected = {}

i = 0
for id_user, songs in songs_per_mood_per_user_filtered.items():
  i += 1
  if i == 101:
    break

  before = len(songs['-']) + len(songs['~']) + len(songs['+'])

  songs_selected[id_user] = {'-':[songs['-'][0]],'~':[songs['~'][0]],'+':[songs['+'][0]]}
  songs['-'].pop(0)
  songs['~'].pop(0)
  songs['+'].pop(0)

  after = len(songs['-']) + len(songs['~']) + len(songs['+'])

  print(before-after)

with open('./data/songs_selected.json', 'w') as file:
  json.dump(songs_selected, file, sort_keys=True)
