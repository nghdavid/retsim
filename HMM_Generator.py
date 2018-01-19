#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 14:57:16 2017

@author: nghdavid
"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import mat4py as m4p
from math import sqrt,pow
import cv2
import os
import sys

os.chdir("/home/nghdavid/Desktop/COREM-master/COREM/input_sequences/Weberlaw/HMM_sequence")
## Parameter Setting
frame_we_want = int(sys.argv[1])
dt = float(sys.argv[2])*0.001
G_HMM = float(sys.argv[3])



#num_frame = frame_we_want + 120
T = np.arange(0.0,frame_we_want+100,dt)
D_HMM = 2700000
omega = G_HMM/2.12

Xarray = np.zeros(len(T))

Vx = np.zeros(len(T))

## HMM sequence
for t in range(len(T)-1):
	Xarray[t+1] = Xarray[t] + Vx[t]*dt
	Vx[t+1] = (1 - G_HMM*dt)*Vx[t] + sqrt(dt*D_HMM)*(np.random.normal(0.0,1.0)) - pow(omega,2)*Xarray[t]*dt
final_seq = Xarray[len(T)-frame_we_want-100:]


maximum = np.ones(final_seq.shape)*np.max(final_seq)
minimum = np.ones(final_seq.shape)*np.min(final_seq)
diff = maximum - minimum
normalized = (final_seq - minimum)/diff
## Create photo
for photo in range(len(final_seq)):
	big_pic = np.ones((25,25),np.double)*(-1)
	pic = np.ones((15,15),np.double)*(normalized[photo])*250
	big_pic[5:20,5:20] = pic
	num = photo + 1
		
		
	if num < 10:
		   number = "0000" + str(num)
	elif num < 100:
		   number = "000" + str(num)
	elif num < 1000:
		   number = "00" + str(num)
	elif num < 10000:
		   number = "0" + str(num)
	else:
		   number = str(num)
	filename = "stimulus. " + number + ".pgm"
		
	cv2.imwrite(filename,big_pic)
os.chdir('/home/nghdavid/Desktop/input_sequence/HMM_sequence')
#data = {}
#data['final_seq'] = normalized.tolist()
np.save('stimulus.npy',normalized)
#m4p.savemat('final_seq_HMM.mat', data)
