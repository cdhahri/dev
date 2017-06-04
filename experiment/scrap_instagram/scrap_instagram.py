#!/usr/bin/python

import codecs, json, requests
from datetime import datetime
from requests.exceptions import ConnectionError

today = "{:%Y.%m.%d}".format(datetime.now())

with open('../ids/instagram.json', 'r') as file:
  ids = json.load(file)

#ids = ['gd_hayato','naopi36','crwmsk','saorinrinririn87','strawberry.rori','xiongsishenye']

for user_id in ids:
  r = requests.get('https://www.instagram.com/{}'.format(user_id))
  if r.status_code == 200:
    data = r.text.split('window._sharedData = ')[1].split(';</script>')[0]
    data = json.loads(data)['entry_data']['ProfilePage'][0]['user']['media']
    try:
      with open('./daily/{}.json'.format(user_id), 'r') as file:
        history = json.load(file)
    except IOError as e:
      if str(e) == '[Errno 2] No such file or directory: \'./daily/{}.json\''.format(user_id):
        history = {}
    history[today] = data
    with open('./daily/{}.json'.format(user_id), 'w') as file:
      json.dump(history, file, sort_keys=True)
#    r = requests.get('https://www.instagram.com/p/{}'.format(data['nodes'][0]['code']))
#    if r.status_code == 200:
#      with codecs.open('/tmp/instagram/{}.json'.format(data['nodes'][0]['code']), 'w', 'utf-8') as file:
#        file.write(r.text)
#    else:
#      print(data['nodes'][0]['code'])
#      print(r.status_code)
  else:
    print(user_id)
    print(r.status_code)
