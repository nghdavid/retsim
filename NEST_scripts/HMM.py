#!/usr/bin/python3
# coding: utf-8
#Control the overall HMM simulation including COREM and NEST
import nest
import nest.raster_plot
import numpy as np
import matplotlib.pyplot as plt
import mat4py as m4p
import os
import sys
from HMM_script import generateScript

root = "/home/nghdavid/Desktop/COREM-master/COREM/"
# simulation parameters
ganglionCells = 25*25

simTime = int(sys.argv[1])#ms
period = int(sys.argv[2])#ms
G_HMM = int(sys.argv[3])



### root path ###

call = "rm -r " + root + "Retina_scripts/HMM_scripts"
### folder for retina scripts ###
os.system(call)
os.system("mkdir "+root+"Retina_scripts/HMM_scripts")
### Generate Retina Script
Total_time = simTime + 100*period
generateScript(root,Total_time,period)

# Reset kernel and network
nest.ResetKernel()
nest.ResetNetwork()

# Number of threads (must be 1) and resolution (the same of the retina script)
nest.SetKernelStatus({"local_num_threads": 1,'resolution': 1.0})

# Install module just once
model = nest.Models(mtype='nodes',sel='corem')
if not model:
    nest.Install("corem_module")

# Create spike detector and spiking nodes
mult = nest.Create('spike_detector',1)
spikingGanglion=nest.Create('iaf_psc_alpha',ganglionCells,{'E_L':-56.0})
nest.Connect(spikingGanglion,mult)

# COREM nodes
for i in range(0,ganglionCells):
    g=nest.Create('corem',1,{'port':float(i),'file':"Retina_scripts/HMM_scripts/HMM.py"})
    nest.Connect(g,[spikingGanglion[i]])

# Simulation
nest.Simulate(Total_time)

def _from_memory(detec):
    ev = nest.GetStatus(detec, "events")[0]
    return ev["times"], ev["senders"]
time, gids = _from_memory(mult)

#Save data to matlab
num_node = 1215#nest.GetStatus(mult)[0]['n_events']
print (num_node)
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
spikes = {}
for i in range(num_node):
    variable = 'Spikes' + str(i+1)
    #data[variable] = dictlist[i][1]
    spikes[i+1] = dictlist[i][1] 


data['num_node'] = num_node
data['sim_time'] = simTime


os.chdir('/home/nghdavid/Desktop/data/')

#m4p.savemat('spikes.mat', data)
np.save('spikes.npy', spikes) 


# Raster plot
nest.raster_plot.from_device(mult,hist=False)
plt.savefig('raster_plot.png')


os._exit(1)

