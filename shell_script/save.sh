cd ~/Desktop/HMM_data/
G_HMM="corr$1"
mkdir $G_HMM
cd "$G_HMM"
time="$2s"
mkdir $time
cd "$time"
period="$3ms"
mkdir $period
num_file=$(ls "$period"/ | wc -l)
cd "$period"

num_file=$(($num_file+1))
mkdir $num_file
cd "$num_file"
mkdir spike
mkdir input_sequence
mkdir MI_curve
mkdir ganglion_MI
mkdir Gb_MI
mkdir Sp_MI
mkdir SNL_ganglion
cd ~/Desktop/COREM-master/COREM
cp -R results/ ~/Desktop/HMM_data/"$G_HMM"/"$time"/"$period"/"$num_file"/

cp -R ~/Desktop/input_sequence/HMM_sequence/* ~/Desktop/HMM_data/"$G_HMM"/"$time"/"$period"/"$num_file"/input_sequence/

cp -R ~/Desktop/data/* ~/Desktop/HMM_data/"$G_HMM"/"$time"/"$period"/"$num_file"/
mv -f ~/Desktop/HMM_data/"$G_HMM"/"$time"/"$period"/"$num_file"/spikes.npy ~/Desktop/HMM_data/"$G_HMM"/"$time"/"$period"/"$num_file"/spike
cp -R ~/Desktop/HMM/* ~/Desktop/HMM_data/"$G_HMM"/"$time"/"$period"/"$num_file"/
cd ~/Desktop/HMM_data/"$G_HMM"/"$time"/"$period"/"$num_file"/
unset period
unset G_HMM
unset time

