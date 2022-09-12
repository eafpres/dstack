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
import matplotlib.pyplot as plt
import sys
import os
#
#%% configure
#
my_os = sys.platform
print('found OS ', my_os)
print('user is: ', os.environ.get('USER'))
print('working directory is: ', os.getcwd())
#
#%% data
#
data = pd.read_csv('data/parabolic_data.csv')
#
#%% stats
#
print('data summary')
print(data.describe())
#
#%% visualize
#
fig, ax = plt.subplots(figsize = (9, 9))
ax.scatter(data['x'], data['y'])
plt.savefig('parabolic.jpg')
#