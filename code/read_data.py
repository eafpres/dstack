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
data = pd.read_csv('https://eaf-test-dstack.s3.amazonaws.com/artifacts/eafpres/dstack/light-otter-1%2C%2C0/data%5Cparabolic_data.csv')
#
#%% stats
#
print('data summary')
print(data.describe())
#