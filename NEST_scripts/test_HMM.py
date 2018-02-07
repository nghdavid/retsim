#!/usr/bin/python
# coding: utf-8

import nest
import nest.raster_plot
import numpy as np
import matplotlib.pyplot as plt
import mat4py as m4p
import os
import sys

# simulation parameters
ganglionCells = 25*25

simTime = sys.argv[1]

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
    g=nest.Create('corem',1,{'port':float(i),'file':"Retina_scripts/test_HMM.py"})
    nest.Connect(g,[spikingGanglion[i]])

# Simulation
nest.Simulate(simTime)

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
for i in range(num_node):
    variable = 'Spikes' + str(i+1)
    data[variable] = dictlist[i][1]    
data['num_node'] = num_node
data['sim_time'] = simTime

os.chdir('/home/nghdavid/Desktop/data/')

m4p.savemat('spikes.mat', data)



# Raster plot
nest.raster_plot.from_device(mult,hist=False)
plt.show()

os._exit(1)
#sys.exit(1)
