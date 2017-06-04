#!/usr/bin/python

import json

with open('/vagrant/src/track/data/ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  with open('/vagrant/src/track/data/fitbit/{}.json'.format(user_id), 'r') as file:
    fitbit_activities = json.load(file)

  steps = {}
  floors = {}
  distance = {}
  for key in sorted(fitbit_activities.keys()):
    import re
    match = re.match('^(.+)-(.+)-(.+)-.+$', key)
    day = '{}-{}-{}'.format(match.group(1),match.group(2),match.group(3))
    if day not in steps:
      steps[day] = []
      floors[day] = []
      distance[day] = []
    steps[day].append(fitbit_activities[key]['lifetime_steps'])
    floors[day].append(fitbit_activities[key]['lifetime_floors'])
    distance[day].append(fitbit_activities[key]['lifetime_distance'])

  w = '../tweets_selected/features_step2/10/{}fitbit_steps.json'.format(user_id)
  with open(w, 'w') as file:
    json.dump(steps, file, sort_keys=True)
  w = '../tweets_selected/features_step2/10/{}fitbit_floors.json'.format(user_id)
  with open(w, 'w') as file:
    json.dump(floors, file, sort_keys=True)
  w = '../tweets_selected/features_step2/10/{}fitbit_distance.json'.format(user_id)
  with open(w, 'w') as file:
    json.dump(distance, file, sort_keys=True)
