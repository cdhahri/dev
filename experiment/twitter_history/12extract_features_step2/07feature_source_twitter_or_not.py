#!/usr/bin/python3

sources = {
  '<a href="http://blackberry.com/twitter" rel="nofollow">Twitter for BlackBerry®</a>':None,
  '<a href="http://dashboard.twitter.com" rel="nofollow">Twitter Dashboard for iPhone</a>':None,
  '<a href="http://itunes.apple.com/us/app/twitter/id409789998?mt=12" rel="nofollow">Twitter for Mac</a>':None,
  '<a href="http://mobile.twitter.com" rel="nofollow">Mobile Web</a>':None,
  '<a href="https://about.twitter.com/products/tweetdeck" rel="nofollow">TweetDeck</a>':None,
  '<a href="https://dev.twitter.com/docs/tfw" rel="nofollow">Twitter for Websites</a>':None,
  '<a href="https://mobile.twitter.com" rel="nofollow">Mobile Web (M2)</a>':None,
  '<a href="https://mobile.twitter.com" rel="nofollow">Mobile Web (M5)</a>':None,
  '<a href="https://twitter.com/download/android" rel="nofollow">Twitter for  Android</a>':None,
  '<a href="https://twitter.com/download/android" rel="nofollow">Twitter for Android Tablets</a>':None,
  '<a href="https://twitter.com/download/iphone" rel="nofollow">Twitter for Apple Watch</a>':None,
  '<a href="http://twitter.com/devices" rel="nofollow">Twitter MMS</a>':None,
  '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>':None,
  '<a href="http://twitter.com/#!/download/ipad" rel="nofollow">Twitter for iPad</a>':None,
  '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>':None,
  '<a href="http://twitter.com/oneshot" rel="nofollow">OneShot - Take screenshots</a>':None,
  '<a href="http://twitter.com" rel="nofollow">Twitter</a>':None,
  '<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>':None,
  '<a href="http://twitter.com/samsungmobile" rel="nofollow">New Samsung Galaxy</a>':None,
  '<a href="http://www.twitter.com" rel="nofollow">Twitter for BlackBerry</a>':None,
  '<a href="http://www.twitter.com" rel="nofollow">Twitter for Windows</a>':None,
  '<a href="http://www.twitter.com" rel="nofollow">Twitter for Windows Phone</a>':None,
}

percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentages = [10]

import json

with open('../../ids/twitter.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  for percentage in percentages:
    r = '../output/{}tweets_selected.json'.format(user_id)
    w = '../output/{}source_twitter_or_not.json'.format(user_id)

    try:
      with open(r, 'r') as file:
        tweets_hash = json.load(file)
    except FileNotFoundError as e:
      print(e)
      continue

    tweets = []
    for key in sorted(tweets_hash.keys()):
      tweets.append(tweets_hash[key])

    feature = []
    for tweet in tweets:
      if tweet['source'] in sources:
        feature.append(1)
      else:
        feature.append(0)

    with open(w, 'w') as file:
      json.dump(feature, file)
