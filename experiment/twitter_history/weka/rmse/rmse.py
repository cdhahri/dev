#!/usr/bin/python3

import json
with open('./rmse.json', 'r') as file:
  rmse = json.load(file)

import numpy as np
a = np.array([rmse])
print(np.mean(a))
print(np.var(a))
