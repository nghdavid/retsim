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
nbin = 25
rank = 100
MI_Limit = 20
shift = 5
forward = int(np.ceil(shift/period))
backward = int(np.ceil(shift/period))
taus = np.linspace(-2,2,401)# Notice period
pwd = os.getcwd()
read_stimulus = np.load(pwd+"/input_sequence/stimulus.npy")
read_stimulus = read_stimulus[-int(sim_time/period):]
stt = read_stimulus[forward:len(read_stimulus)-backward]

read_spikes = np.load(pwd+"/spike/spikes.npy")
tst = np.arange(0,sim_time-2*shift+period,period)

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
def time_shift(spt,shift,tau,sim_time):
    shift_spt = []
    if tau != 0:
        for spiking_time in spt:
            if spiking_time >= (shift-tau) and spiking_time <= (sim_time-tau-shift):
                shift_spt.append(spiking_time-shift+tau)
    else:
        for spiking_time in spt:
            if spiking_time >= shift and spiking_time <= (sim_time-shift):
                shift_spt.append(spiking_time-shift)
    return shift_spt
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


channel_we_want ,spikes = process_spike(read_spikes,rank)


id = 1
peak = []
Mutual_Information = {}
tss = binning(nbin,sim_time,period,stt)

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
    mik = []
    mik_shuffle = []
    
    for t in taus:
        shift_spt = time_shift(spt,shift,t,sim_time)
        bsz = period
        bsp ,bin_edges = np.histogram(shift_spt,bins=tst)
        
        nz = max(bsp)+1 #number of most spike + 1
        
        xedge = range(nbin+1)
        yedge = range(nz+1)
        
        pxy, xedges, yedges = np.histogram2d(tss,bsp,bins=(xedge,yedge))
        
        
        mik.append(MI(pxy))

        bsp_shuffle = np.random.permutation(bsp)
        shuffle_pxy, xedges, yedges = np.histogram2d(tss,bsp_shuffle,bins=(xedge,yedge))
        mik_shuffle.append(MI(shuffle_pxy))
    
    
    
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
for i in range(-200,250,10):
    num_peak[round(i)] = 0
    x.append(round(i))
    y.append(round(i))
for j in peak_time:
    num = num_peak[round(j)]
    num_peak[round(j)] = num + 1

for key in num_peak:
    y[x.index(key)] = num_peak[key]
    

plt.figure(0)
plt.bar(x,y,10,align='center')
plt.ylim([0,100])
plt.xlim([-50,20])
plt.xticks(range(-50,20,10))
plt.title("Peak Distribution")
plt.xlabel("peak (ms)")
plt.ylabel("frequency")

plt.savefig("peak.jpg")
