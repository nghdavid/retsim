#!/bin/bash
Sim_Time=$1 #50000
Period=$2 #50 
G_HMM=$3 #5
Num_Frame=$(($Sim_Time/$Period))

./remove.sh
./HMM_Generator.sh $Num_Frame $Period $G_HMM

cd ~/
. ./nest.sh

python NEST_scripts/adaptation.py $Sim_Time $Period $G_HMM

./corem Retina_scripts/adaptation_scripts/adaptation.py

. ./save_adaptation.sh $G_HMM $(($Sim_Time/1000)) $Period

#python Vis_stimulus.py $(($Sim_Time/1000)) $Period
cd /home/nghdavid/Desktop/COREM-master/COREM

