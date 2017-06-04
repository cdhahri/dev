#!/usr/bin/python

import json
import numpy as np

for classifier in ['ibk.grep','linreg.grep','multipercep.grep','reptree.grep','smoreg.grep']:
  with open(classifier, 'r') as file:
    rmse = json.load(file)
  print(classifier)
  a = np.array([rmse])
  print(np.mean(a))
  print(np.var(a))
