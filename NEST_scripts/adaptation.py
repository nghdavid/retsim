#!/usr/bin/python3
# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt
import mat4py as m4p
import os
import sys
from adaptation_script import generateScript

root = "/home/nghdavid/Desktop/COREM-master/COREM/"
# simulation parameters
ganglionCells = 25*25

simTime = int(sys.argv[1])#ms
period = int(sys.argv[2])#ms
G_HMM = int(sys.argv[3])



### root path ###

call = "rm -r " + root + "Retina_scripts/adaptation_scripts"
### folder for retina scripts ###
os.system(call)
os.system("mkdir "+root+"Retina_scripts/adaptation_scripts")
### Generate Retina Script
Total_time = simTime + 100*period
generateScript(root,Total_time,period)


os._exit(1)

