#The code that calculate the mutual information between stimulus and firing rate with time shift


import matplotlib as mpl
mpl.use('nbagg')
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.io import loadmat
import numpy as np
import operator
import os
import sys
sim_time = int(sys.argv[1])#second
period = float(sys.argv[2])/1000.0#second
nbin = 25#number of bins
rank = 100
MI_Limit = 20
taus = np.linspace(-4,4,161)# Notice period
pwd = os.getcwd()
read_stimulus = np.load(pwd+"/input_sequence/stimulus.npy")
read_stimulus = read_stimulus[-int(sim_time/period):]#Delete the anterior part that is not stable
stt = read_stimulus
read_spikes = np.load(pwd+"/spike/spikes.npy")
tst = np.arange(0,sim_time,period)

# spikes are binned first
def binning_spike(period,spt):    
    bsz = period
    bsp = []
    tn = 0 
    for t in spt:
        while t>tn:
            bsp.append(0)
            tn = len(bsp)*bsz
        bsp[-1] += 1
    nz = max(bsp)+1 #number of most spike + 1
    return bsp, nz
# sort the spike
def process_spike(read_spikes,rank):
    spike = read_spikes.item()
    num_channel = len(spike)
    num_spike = {}
    for channel in spike:
        num_spike[channel] = len(spike[channel])
    sorted_spike = sorted(num_spike.items(), key=operator.itemgetter(1))
    channel_we_want = sorted_spike[-rank:]
    return channel_we_want, spike

# discretize periods with equally-binned indices
def binning(nbin,sim_time,period,stt):
    
    tsi = np.argsort(stt)
    tss = np.array(stt,dtype=int)
    p = 0
    for i in range(0,nbin):
        ii = len(stt)*(i+1)//nbin
        tss[tsi[p:ii]] = i
        p = ii
    return tss
#Calculate MI
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
#Calculate joint distribution
def mi_kevin(tau,nbin,nz,bsp,period,tss,tst):
    ii = 0
    pxy = np.zeros([nbin,nz])
    for i in range(len(bsp)):
        t = i*period+tau
        while ii<len(tss) and t>tst[ii]: ii += 1
        if i == 10 and tau == 0:
            print (ii)
        if ii==len(tss): break
        pxy[tss[ii]][bsp[i]] += 1
    return MI(pxy)

channel_we_want ,spikes = process_spike(read_spikes,rank)
id = 1
peak = []
Mutual_Information = {}
#Calculate the channel with enough spike
for channel in channel_we_want:
    filename = pwd +"/MI_curve/"+"channel" + str(channel[0]) + ".jpg"
    spike = spikes[channel[0]]
    spt = np.multiply(spike,0.001)
    
    SPT = []
    for t in spt:
        if t > 100*period:
            time = t - 100*period
            SPT.append(time)
    spt = np.array(SPT)
    
    bsp, nz = binning_spike(period,spt)#bin spike
    tss = binning(nbin,sim_time,period,stt)#bin stimulus
    
    bsp_shuffle = np.random.permutation(bsp)
    mik_shuffle = [mi_kevin(t,nbin,nz,bsp_shuffle,period,tss,tst) for t in taus]
    
    mik = [mi_kevin(t,nbin,nz,bsp,period,tss,tst) for t in taus]
    Mutual_Information[channel[0]] = mik
    Max_MI = max(mik)/period
    Max_Time = taus[mik.index(max(mik))]
    peak.append(Max_Time)
    plt.figure(id)
    id = id + 1
    plt.plot(taus,np.array(mik)/period,'b')
    plt.plot(taus,np.array(mik_shuffle)/period,'r-',label="shuffle")
    plt.xlabel("delta t(s)")
    plt.ylabel("mutual information(bits/sec)")
    plt.ylim([0,MI_Limit])
    plt.title("Neuron "+str(channel[0]))
    plt.axvline(Max_Time,ymax=Max_MI/MI_Limit,color='k')
    plt.legend()
    plt.savefig(filename)


np.save('Mutual_Information.npy',Mutual_Information)
peak_time = np.multiply(np.array(peak),1000)
np.save('peak.npy',peak_time)
print (peak_time)

num_peak = {}
x = []
y = []
p = int(period*1000)
for i in range(-200,250,p):
    num_peak[round(i)] = 0
    x.append(round(i))
    y.append(round(i))
for j in peak_time:
    num = num_peak[round(j)]
    num_peak[round(j)] = num + 1


for key in num_peak:
    y[x.index(key)] = num_peak[key]
    

plt.figure(0)
plt.bar(x,y,20,align='center')
plt.ylim([0,100])
plt.xticks(range(-200,250,p))
plt.title("Peak Distribution")
plt.xlabel("peak (ms)")
plt.ylabel("frequency")

plt.savefig("peak.jpg")
