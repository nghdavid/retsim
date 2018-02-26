#Calculate the mutual information between stimulus and SNL_photorecptor

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
nbin = 30
rank = 100
MI_Limit = 100
shift = 5
forward = int(np.ceil(shift/period))
backward = int(np.ceil(shift/period))
taus = np.linspace(-2,2,401)# Notice period
pwd = os.getcwd()
read_stimulus = np.load(pwd+"/input_sequence/stimulus.npy")
read_stimulus = read_stimulus[-int(sim_time/period):]
stt = read_stimulus[forward:len(read_stimulus)-backward]
tst = np.arange(0,sim_time-2*shift,period)

# discretize periods with equally-binned indices
def binning(nbin,stt):
    
    tsi = np.argsort(stt)
    tss = np.array(stt,dtype=int)
    p = 0
    for i in range(0,nbin):
        ii = len(stt)*(i+1)//nbin
        tss[tsi[p:ii]] = i
        p = ii
    return tss

def MI(pxy):
    px = pxy.sum(axis=1)
    py = pxy.sum(axis=0)
    pxy /= pxy.sum()
    px /= px.sum()
    py /= py.sum()
    mi = 0
    for i in range(len(px)):
        for j in range(len(py)):
            if pxy[i][j]>0: mi += pxy[i][j]*np.log2(pxy[i][j]/(px[i]*py[j]))
    return mi

def mi_kevin(nbin,nz,bsp,period,tss,tst):
    xedge = range(nbin+1)
    yedge = range(nz+1)
    pxy, xedges, yedges = np.histogram2d(tss,bsp,bins=(xedge,yedge))
    print (pxy)
    print (xedges)
    print (yedges)
    return MI(pxy)

id = 1
peak = []
Mutual_Information = {}
tss = binning(nbin,stt)
step_size = 0.001
Forward = int(np.ceil(shift/step_size))
Backward = int(np.ceil(shift/step_size))
for i in range(10,21,1):
	for j in range(10,21,1):
		number=str(i)+str(j)   	   	
		filename = pwd +"/Sp_MI/"+ number + ".jpg"        

		read_Sp = np.loadtxt(pwd+"/results/SNL_photoreceptors"+number)

		mik = []
		mik_shuffle = []
		for t in taus:
			time_shift = int(np.round(t/step_size))
		
			Sp = read_Sp[-int(sim_time/0.001):]
		
			Sp = Sp[Forward-time_shift:len(Sp)-Backward-time_shift]
			shift_Sp = Sp.reshape(-1, 50).mean(axis=1)
		
			shift_tss = binning(nbin,shift_Sp)
			xedge = range(nbin+1)
			yedge = range(nbin+1)
			pxy, xedges, yedges = np.histogram2d(tss,shift_tss,bins=(xedge,yedge))
			mik.append(MI(pxy))

			stt_shuffle = np.random.permutation(shift_Sp)
			shuffle_pxy, xedges, yedges = np.histogram2d(tss,stt_shuffle,bins=(xedge,yedge))
			mik_shuffle.append(MI(shuffle_pxy))
		
		Max_MI = max(mik)/period
		Max_Time = taus[mik.index(max(mik))]
		peak.append(Max_Time)
		

		plt.figure(id)
		id = id + 1
		plt.plot(taus,np.array(mik)/period,'b')
		plt.plot(taus,np.array(mik_shuffle)/period,'r-',label="shuffle")
		plt.ylim([0,MI_Limit])
		plt.xlabel("delta t(s)")
		plt.ylabel("mutual information(bits/sec)")

		plt.axvline(Max_Time,ymax=Max_MI/MI_Limit,color='k')
		plt.legend()

		plt.savefig(filename)
peak_time = np.multiply(np.array(peak),1000)
np.save('peak_Sp.npy',peak_time)
print (peak_time)


num_peak = {}
x = []
y = []
p = int(period*1000)
for i in range(-300,200,10):
    num_peak[round(i)] = 0
    x.append(round(i))
    y.append(round(i))
for j in peak_time:
    if round(j) < 200 and round(j) >-300:	
    	num = num_peak[round(j)]
    	num_peak[round(j)] = num + 1

for key in num_peak:
    y[x.index(key)] = num_peak[key]
    

plt.figure(0)
plt.bar(x,y,20,align='center')
plt.ylim([0,30])
plt.xlim([-300,200])
plt.xticks(range(-250,200,p))
plt.title("Peak Distribution")
plt.xlabel("peak (ms)")
plt.ylabel("frequency")

plt.savefig("peak_Sp.jpg")


