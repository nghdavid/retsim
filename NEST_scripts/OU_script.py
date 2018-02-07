import matplotlib.pyplot as plt
import numpy
import sys
import os

def generateScript(root,SimTime,period):

    text_file = open(root+"Retina_scripts/OU_scripts/OU.py", "w")

    text_file.write(""+

    "retina.TempStep('1')\n"+

    "retina.SimTime('"+
	str(SimTime)+ 
	"')\n"+

    "retina.NumTrials('1')\n"+

    "retina.PixelsPerDegree({'5'})\n"+

    "retina.DisplayDelay('0')\n"+

    "retina.DisplayZoom({'10.0'})\n"+

    "retina.DisplayWindows('3')\n"+

    "retina.Input('sequence','input_sequences/Weberlaw/OU_sequence/',{'InputFramePeriod','"+
str(period)+
"'})\n"+

    "retina.Create('LinearFilter','tmp_photoreceptors',{'type','Gamma','tau','30.0','n','10.0'})\n"+

    "retina.Create('LinearFilter','tmp_horizontal',{'type','Gamma','tau','20.0','n','1.0'})\n"+
    "retina.Create('SingleCompartment','tmp_bipolar',{'number_current_ports','1.0','number_conductance_ports','2.0','Rm','0.0','Cm','100.0','E',{'0.0','0.0'}})\n"+

    "retina.Create('LinearFilter','tmp_amacrine',{'type','Gamma','tau','10.0','n','1.0'})\n"+
    "retina.Create('GaussFilter','Gauss_horizontal',{'sigma','0.3','spaceVariantSigma','False'})\n"+

    "retina.Create('GaussFilter','Gauss_bipolar',{'sigma','0.1','spaceVariantSigma','False'})\n"+

    "retina.Create('GaussFilter','Gauss_amacrine',{'sigma','0.3','spaceVariantSigma','False'})\n"+
    "retina.Create('GaussFilter','Gauss_ganglion',{'sigma','0.2','spaceVariantSigma','False'})\n"+
    "retina.Create('StaticNonLinearity','SNL_photoreceptors',{'slope','-0.1','offset','0.0','exponent','1.0'})\n"+
    "retina.Create('StaticNonLinearity','SNL_horizontal',{'slope','1.0','offset','0.0','exponent','1.0'})\n"+
    "retina.Create('StaticNonLinearity','SNL_amacrine',{'slope','0.2','offset','1.0','exponent','2.0'})\n"+

	"retina.Create('StaticNonLinearity','SNL_bipolar',{'slope','10.0','offset','0.0','exponent','1.0','threshold','0.0'})\n"+
	"retina.Create('StaticNonLinearity','SNL_ganglion',{'slope','5.0','offset','0.0','exponent','1.0'})\n"+
    "retina.Connect('L_cones','tmp_photoreceptors','Current')\n"+
    "retina.Connect('tmp_photoreceptors','SNL_photoreceptors','Current')\n"+

    "retina.Connect('SNL_photoreceptors','Gauss_horizontal','Current')\n"+
    "retina.Connect('Gauss_horizontal','tmp_horizontal','Current')\n"+
    "retina.Connect('tmp_horizontal','SNL_horizontal','Current')\n"+
    "retina.Connect({'SNL_horizontal',-,'SNL_photoreceptors'},'Gauss_bipolar','Current')\n"+

    "retina.Connect('Gauss_bipolar','tmp_bipolar','Current')\n"+
    "retina.Connect('tmp_bipolar','SNL_bipolar','Current')\n"+
    "retina.Connect('SNL_bipolar','Gauss_amacrine','Current')\n"+
    "retina.Connect('Gauss_amacrine','tmp_amacrine','Current')\n"+

    "retina.Connect('tmp_amacrine','SNL_amacrine','Current')\n"+
    "retina.Connect('SNL_amacrine','tmp_bipolar','Conductance')\n"+

    "retina.Connect('SNL_bipolar','Gauss_ganglion','Current')\n"+

    "retina.Connect('Gauss_ganglion','SNL_ganglion','Current')\n"+

    "retina.Connect('SNL_ganglion','Output','Current')\n"
	

+generate_multimeter("Input",0)
+generate_multimeter("Gauss_bipolar",0)
+generate_multimeter("Gauss_amacrine",0)
+generate_multimeter("Gauss_ganglion",0)
+generate_multimeter("Gauss_horizontal",0)
+generate_multimeter("tmp_photoreceptors",0)
+generate_multimeter("tmp_horizontal",0)
+generate_multimeter("tmp_bipolar",0)
+generate_multimeter("tmp_amacrine",0)
+generate_multimeter("SNL_photoreceptors",0)
+generate_multimeter("SNL_ganglion",0)
+generate_multimeter("SNL_amacrine",0)
+generate_multimeter("SNL_bipolar",0)
+generate_multimeter("SNL_ganglion",0)


    )
	
    text_file.close()


def generate_multimeter(name,starttime):
	script = ""
	for i in range(10,21):
		for j in range(10,21):
			script += "retina.multimeter('temporal','"
			script += name
			script += str(i)
			script += str(j)
			script += "','"
			script += name
			script += "',{'x','"
			script += str(i)
			script += "','y','"
			script += str(j)
			script += "'},'Show','False','startTime','"
			script += str(starttime)
			script += "')\n"
	return script

