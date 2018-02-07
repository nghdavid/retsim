import matplotlib as mpl
mpl.use('nbagg')
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.io import loadmat
import numpy as np
import operator
import os
import sys



def ganglion_plot(num,fig_num):
    name = "ganglion" + num
    read_file = open("results/"+name,'r')
    data = read_file.read()
    StringList = data.split('\n')
    ganglion = []
    length = len(StringList)-1
    for num in range(length):
        number = float(StringList[num])
        ganglion.append(number)

    time = np.multiply(np.arange(0,len(ganglion),1),0.001)
    plt.figure(fig_num,figsize=(20, 12), dpi=100)
    plt.plot(time,ganglion)
    plt.xlabel("time (sec)")
    plt.ylabel("voltage")
    plt.title(name)
    plt.ylim([0,120])
    plt.savefig("ganglion/"+name+".jpg")
    #plt.show()
    read_file.close()

for x in range(15,21):
    for y in range(15,21):
        number = str(x) + str(y)
        ganglion_plot(number,int(number))
