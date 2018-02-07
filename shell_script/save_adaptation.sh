cd ~/Desktop/adaptation_data/
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

mkdir input_sequence
mkdir MI_curve

cd ~/Desktop/COREM-master/COREM
cp -R results/ ~/Desktop/adaptation_data/"$G_HMM"/"$time"/"$period"/"$num_file"/

cp -R ~/Desktop/input_sequence/HMM_sequence/* ~/Desktop/adaptation_data/"$G_HMM"/"$time"/"$period"/"$num_file"/input_sequence/

cp -R ~/Desktop/adaptation/* ~/Desktop/adaptation_data/"$G_HMM"/"$time"/"$period"/"$num_file"/
cd ~/Desktop/adaptation_data/"$G_HMM"/"$time"/"$period"/"$num_file"/
unset period
unset G_HMM
unset time
