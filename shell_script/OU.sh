#!/bin/bash
Sim_Time=$1 #50000
Period=$2 #50 
G_HMM=$3 #5
Num_Frame=$(($Sim_Time/$Period))

./remove.sh
./OU_Generator.sh $Num_Frame $Period $G_HMM

cd ~/
. ./nest.sh

python NEST_scripts/OU.py $Sim_Time $Period $G_HMM

. ./save_OU.sh $G_HMM $(($Sim_Time/1000)) $Period

python moving_window.py $(($Sim_Time/1000)) $Period
mkdir ganglion
#python ganglion_plot.py
python Sp_stimulus.py $(($Sim_Time/1000)) $Period
python Gb_stimulus.py $(($Sim_Time/1000)) $Period
python ganglion_stimulus.py $(($Sim_Time/1000)) $Period
python stimulus.py $(($Sim_Time/1000)) $Period
cd /home/nghdavid/Desktop/COREM-master/COREM


