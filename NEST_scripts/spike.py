#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:20:00 2017

@author: nghdavid
"""
import numpy as np
import matplotlib.pyplot as plt
import mat4py as m4p
time = [43,43,50]
gids = [185,155,155]
num_node = 200
dict = {}
for num in range(num_node):
    dict[num] = []
for i in range(len(gids)):
    gid = gids[i]
    dict[gid].append(time[i])
dictlist = []
for key, value in dict.items():
    temp = [key,value]
    dictlist.append(temp)
data = {}
for i in range(num_node):
    variable = 'Spikes' + str(i+1)
    data[variable] = dictlist[i][1]    

m4p.savemat('test.mat', data)
