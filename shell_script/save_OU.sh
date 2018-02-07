cd ~/Desktop/OU_data/
G_OU="corr$1"
mkdir $G_OU
cd "$G_OU"
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
cp -R results/ ~/Desktop/OU_data/"$G_OU"/"$time"/"$period"/"$num_file"/

cp -R ~/Desktop/input_sequence/OU_sequence/* ~/Desktop/OU_data/"$G_OU"/"$time"/"$period"/"$num_file"/input_sequence/

cp -R ~/Desktop/data/* ~/Desktop/OU_data/"$G_OU"/"$time"/"$period"/"$num_file"/
mv -f ~/Desktop/OU_data/"$G_OU"/"$time"/"$period"/"$num_file"/spikes.npy ~/Desktop/OU_data/"$G_OU"/"$time"/"$period"/"$num_file"/spike
cp -R ~/Desktop/OU/* ~/Desktop/OU_data/"$G_OU"/"$time"/"$period"/"$num_file"/
cd ~/Desktop/OU_data/"$G_OU"/"$time"/"$period"/"$num_file"/
unset period
unset G_OU
unset time
