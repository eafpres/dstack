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