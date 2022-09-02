#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 17:55:26 2022

@author: eafpres
"""
#
#%% libraries
#
import pandas as pd
import sys
#
#%% configure
#
my_os = sys.platform
if my_os == 'linux':
  path_prefix = '/mnt/c'
else:
  path_prefix = 'C:'
  #
path = path_prefix + '/eaf llc/aa-analytics and bi/dstack/'
#
#%% data
#
data = pd.read_csv(path + 'data/parabolic_data.csv')
#
#%% stats
#
print('data summary')
print(data.describe())
#