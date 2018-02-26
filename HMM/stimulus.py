#Plot the intensity of stimulus
import matplotlib as mpl
mpl.use('nbagg')
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.io import loadmat
import numpy as np
import operator
import os
import sys
sim_time = int(sys.argv[1])
period = float(sys.argv[2])/1000.0
pwd = os.getcwd()
read_stimulus = np.load(pwd+"/input_sequence/stimulus.npy")
stt = read_stimulus[-int(sim_time/period):]
time = np.arange(0,sim_time,period)
plt.figure(1,figsize=(20, 12), dpi=100)
plt.plot(time,stt)
plt.xlabel("time (sec)")
plt.ylabel("intensity")
plt.title("stimulus")
plt.savefig('stimulus.jpg')


