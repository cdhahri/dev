#!/usr/bin/python3

percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentages = [10]

import csv
import json
import itertools
        
with open('../ids/twitter.json', 'r') as file:
  ids = json.load(file)

ids = ['02_lve','1715m323','313131xuanxiang','9_1020','aa01367231','bmogami','can_dqx','chibi_chika0524','chinyan1019','CoccoSicario','daisyxdaisy76','emataro_2','eryka_anvil','fumiaki246','G_O_N_A','HidamaririM','hikaruma0920','Hivernation_','hulalomi','ice_Cosxxx','jhsuivbs8','kanntada01','kikiki712','kkskze','KNora0013','k_n_t_9497','ko5ji4ko5','kossunsun8','kou_NEWSKOOL','kuni365','lllymklll','Lynntarou333','m1991h_720','maiisy555','manamana_714','MasRicoms5','mayashiba0112','meeeeesuke','miharu_masako','mikamiemi','mikorinmiko','milkyway1115','minochaaan','MonmaRui','nachan7373','Nanacafenana','nanairobega','NARI77Arakawa','nbhr000','nosu03','notupo_san','ntm_hsmt','nunununu_can','_ohyoso_','OotakeWw','precariato','puddingpan1','QaMxddis6JECRCn','R0i9C2h9a','RadioListener06','raiki_mama','ramunecafetrunk','rhrhk','ryan_naoto','sayak_tn','Senyoujizi','shibaaask11','shimizoon','shunabroad','siki_33','sionin7','snuuufkin','st516a','stim588','StrippedRabbit','suekiyo','sugamira789','SUGlK0','takoba0504','tekitoYoshi','umashikamomo','Uriel09zAlexis','utaxx324','willbuono','xxmarchxx','yahata8','ys196764','yUca0914','yuka961007','yulitennis','yusuke761001','zenkaigirl']

for user_id in ids:
  for percentage in percentages:
    r = './output/{}aggregated.json'.format(user_id)
    w = './output/weka/{}weka.csv'.format(user_id)

    try:
      with open(r, 'r') as file:
        byday_aggregated = json.load(file)
    except FileNotFoundError as e:
      print(e)
      continue

    with open(w, 'w', newline='', encoding='utf-8') as file:
      csv_writer = csv.writer(file, delimiter=',')
      csv_writer.writerow(['hashtags_count','mentions_count','favourites_count','media_count','week','day_night','active_passive','mentions','top_mentions','coordinates','target'])
      # csv_writer.writerow(['count_all_capital','count_exclamation_mark','count_question_mark','count_negative_word','count_positive_word','exist_more_than_three_dots','exist_more_than_three_vowels','target'])
      for key in sorted(byday_aggregated.keys()):
        mentions = byday_aggregated[key]['mentions']
        if len(mentions) == 0:
          mentions = [-1]
        top_mentions = byday_aggregated[key]['top_mentions']
        if len(top_mentions) == 0:
          top_mentions = [-1]
        coordinates = byday_aggregated[key]['coordinates']
        if len(coordinates) == 0:
          coordinates = [-1]
  #      a = [mentions, top_mentions, coordinates]
  #      products = list(itertools.product(*a))
  #      for prod in products:
        csv_writer.writerow([
          byday_aggregated[key]['hashtags_count'],
          byday_aggregated[key]['mentions_count'],
          byday_aggregated[key]['favourites_count'],
          byday_aggregated[key]['media_count'],
          #byday_aggregated[key]['source'],
          byday_aggregated[key]['week'],
          byday_aggregated[key]['day_night'],
          byday_aggregated[key]['active_passive'],
            # byday_aggregated[key]['mentions'],
            # byday_aggregated[key]['top_mentions'],
            # byday_aggregated[key]['coordinates'],
         mentions[0],
         top_mentions[0],
         coordinates[0],

          # byday_aggregated[key]['count_all_capital'],
          # byday_aggregated[key]['count_exclamation_mark'],
          # byday_aggregated[key]['count_question_mark'],
          # byday_aggregated[key]['count_negative_word'],
          # byday_aggregated[key]['count_positive_word'],
          # byday_aggregated[key]['exist_more_than_three_dots'],
          # byday_aggregated[key]['exist_more_than_three_vowels'],

  #        prod[0], NO
  #        prod[1], NO
  #        prod[2], NO
          byday_aggregated[key]['_target']
         ])

  '''
  w = '/vagrant/data/osn-data/features_step3/aggregated/weka/all.csv'.format(user_id)
  with open(w, 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(['hashtags_count','mentions_count','favourites_count','media_count','source','week','day_night','active_passive','mentions','coordinates','top_mentions','target'])
    for user_id in ids:
      r = '/vagrant/data/osn-data/features_step3/aggregated/{}.json'.format(user_id)
      with open(r, 'r') as file:
        byday_aggregated = json.load(file)

      for key in sorted(byday_aggregated.keys()):
        csv_writer.writerow([
          byday_aggregated[key]['hashtags_count'],
          byday_aggregated[key]['mentions_count'],
          byday_aggregated[key]['favourites_count'],
          byday_aggregated[key]['media_count'],
          byday_aggregated[key]['source'],
          byday_aggregated[key]['week'],
          byday_aggregated[key]['day_night'],
          byday_aggregated[key]['active_passive'],
          byday_aggregated[key]['mentions'],
          byday_aggregated[key]['coordinates'],
          byday_aggregated[key]['top_mentions'],
          byday_aggregated[key]['_target']
        ])
  '''
