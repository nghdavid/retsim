import matplotlib.pyplot as plt
import numpy
import sys
import os

def generateScript(root,SimTime,period):

    text_file = open(root+"Retina_scripts/adaptation_scripts/adaptation.py", "w")

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

    "retina.Input('sequence','input_sequences/Weberlaw/HMM_sequence/',{'InputFramePeriod','"+
str(period)+
"'})\n"+

    "retina.Create('LinearFilter','tmp_tauR',{'type','Gamma','tau','0.49','n','0.0'})\n"+

    "retina.Create('LinearFilter','tmp_tauE',{'type','Gamma','tau','16.8','n','0.0'})\n"+
    "retina.Create('SingleCompartment','calcium_feedback_SC',{'number_current_ports','1.0','number_conductance_ports','2.0','Rm','0.0','Cm','1.0','E',{'0.0','0.0'}})\n"+

    "retina.Create('LinearFilter','tmp_tauC',{'type','Gamma','tau','2.89','n','0.0'})\n"+

    "retina.Create('LinearFilter','tmp_taum',{'type','Gamma','tau','4.0','n','0.0'})\n"+

    "retina.Create('LinearFilter','tmp_tauis',{'type','Gamma','tau','56.9','n','0.0'})\n"+
    "retina.Create('LinearFilter','tmp_tau1',{'type','Gamma','tau','4.0','n','0.0'})\n"+
    "retina.Create('LinearFilter','tmp_tau2',{'type','Gamma','tau','4.0','n','0.0'})\n"+
    "retina.Create('LinearFilter','tmp_tauh',{'type','Gamma','tau','20.0','n','0.0'})\n"+

    "retina.Create('StaticNonLinearity','beta',{'slope','0.000163','offset','0.0028','exponent','1.0'})\n"+

	"retina.Create('StaticNonLinearity','X',{'slope','1.0','offset','0.0','exponent','1.0'})\n"+
	"retina.Create('StaticNonLinearity','1_div_alpha',{'slope','0.0908','offset','1.0','exponent','4.0'})\n"+
    "retina.Create('StaticNonLinearity','alpha',{'slope','1.0','offset','0.0001','exponent','-1.0'})\n"+
    "retina.Create('StaticNonLinearity','ais',{'slope','0.0709','offset','0.0','exponent','0.678'})\n"+

    "retina.Create('StaticNonLinearity','Vis',{'slope','1.0','offset','-13.9','exponent','1.0'})\n"+
    "retina.Create('StaticNonLinearity','gs',{'slope','0.5','offset','0.0','exponent','1.0'})\n"+
    "retina.Connect('L_cones','tmp_tauR','Current')\n"+
    "retina.Connect('tmp_tauR','tmp_tauE','Current')\n"+

    "retina.Connect('tmp_tauE','beta','Current')\n"+
    "retina.Connect('alpha','calcium_feedback_SC','Current')\n"+
    "retina.Connect('beta','calcium_feedback_SC','Conductance')\n"+
    "retina.Connect('calcium_feedback_SC','X','Current')\n"+

    "retina.Connect('X','tmp_tauC','Current')\n"+
    "retina.Connect('tmp_tauC','1_div_alpha','Current')\n"+

    "retina.Connect('1_div_alpha','alpha','Current')\n"+


    "retina.Connect({'X',/,'tmp_tauis'},'tmp_taum','Current')\n"+

    "retina.Connect('tmp_taum','ais','Current')\n"+
	"retina.Connect('ais','tmp_tauis','Current')\n"+
	"retina.Connect('tmp_taum','Vis','Current')\n"+

	"retina.Connect({'Vis',-,'tmp_tauh'},'gs','Current')\n"+
	"retina.Connect('gs','tmp_tau1','Current')\n"+
	"retina.Connect('tmp_tau1','tmp_tau2','Current')\n"+
	"retina.Connect('tmp_tau2','tmp_tauh','Current')\n"+ 
	"retina.Show('X','True','margin','0')\n"+
	"retina.Show('gs','True','margin','0')\n"+
	"retina.Show('tmp_tau1','True','margin','0')\n"+generate_multimeter("Vis",0)
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
            script += "','Vis',{'x','"
            script += str(i)
            script += "','y','"
            script += str(j)
            script += "'},'Show','False','startTime','"
            script += str(starttime)
            script += "')\n"
    return script

