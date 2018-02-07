###################################################################################
##                                                                               ##
## With this retina model our aim is to show an overview of the main features    ##
## that can be configured in the retina script. The retina model implemented     ##
## in this script processes an input sequence of images based on a general       ##
## retina architecture that includes all neuron types. Temporal evolution and    ##
## spatial arrangement of some neurons' membrane potentials are recorded by      ##
## multimeters and displayed during and after simulation.                        ##
##                                                                               ##
## Author: Pablo Martinez                                                        ##
## email: pablomc@ugr.es                                                         ##
##                                                                               ##
###################################################################################


### Simulation parameters ###

retina.TempStep('1') # simulation step (in ms)
retina.SimTime('500000') # simulation time (in ms)
retina.NumTrials('1') # number of trials
retina.PixelsPerDegree({'5'}) # pixels per degree of visual angle
retina.DisplayDelay('0') # display delay
retina.DisplayZoom({'10.0'}) # display zoom
retina.DisplayWindows('3') # Display windows per row

### Visual input ###

# Folder that contains the input sequence
retina.Input('sequence','input_sequences/Weberlaw/OU_sequence/',{'InputFramePeriod','50'})

### Creation of computational retinal microcircuits ###

# Temporal modules
retina.Create('LinearFilter','tmp_photoreceptors',{'type','Gamma','tau','30.0','n','10.0'})
retina.Create('LinearFilter','tmp_horizontal',{'type','Gamma','tau','20.0','n','1.0'})
retina.Create('SingleCompartment','tmp_bipolar',{'number_current_ports','1.0','number_conductance_ports','2.0','Rm','0.0','Cm','100.0','E',{'0.0','0.0'}})
retina.Create('LinearFilter','tmp_amacrine',{'type','Gamma','tau','10.0','n','1.0'})

# Spatial filters
retina.Create('GaussFilter','Gauss_horizontal',{'sigma','0.3','spaceVariantSigma','False'})
retina.Create('GaussFilter','Gauss_bipolar',{'sigma','0.1','spaceVariantSigma','False'})
retina.Create('GaussFilter','Gauss_amacrine',{'sigma','0.3','spaceVariantSigma','False'})
retina.Create('GaussFilter','Gauss_ganglion',{'sigma','0.2','spaceVariantSigma','False'})

# Nonlinearities
retina.Create('StaticNonLinearity','SNL_photoreceptors',{'slope','-0.1','offset','0.0','exponent','1.0'})
retina.Create('StaticNonLinearity','SNL_horizontal',{'slope','1.0','offset','0.0','exponent','1.0'})
retina.Create('StaticNonLinearity','SNL_amacrine',{'slope','0.2','offset','1.0','exponent','2.0'})
retina.Create('StaticNonLinearity','SNL_bipolar',{'slope','10.0','offset','0.0','exponent','1.0','threshold','0.0'})
retina.Create('StaticNonLinearity','SNL_ganglion',{'slope','5.0','offset','0.0','exponent','1.0'})

### Connections ###

# Phototransduction
retina.Connect('L_cones','tmp_photoreceptors','Current')
retina.Connect('tmp_photoreceptors','SNL_photoreceptors','Current')

# Horizontal cells
retina.Connect('SNL_photoreceptors','Gauss_horizontal','Current')
retina.Connect('Gauss_horizontal','tmp_horizontal','Current')
retina.Connect('tmp_horizontal','SNL_horizontal','Current')

# Subtraction at Outer Plexiform Layer
retina.Connect({'SNL_horizontal',-,'SNL_photoreceptors'},'Gauss_bipolar','Current')
retina.Connect('Gauss_bipolar','tmp_bipolar','Current')
retina.Connect('tmp_bipolar','SNL_bipolar','Current')

# Gain control at Inner Plexiform Layer
retina.Connect('SNL_bipolar','Gauss_amacrine','Current')
retina.Connect('Gauss_amacrine','tmp_amacrine','Current')
retina.Connect('tmp_amacrine','SNL_amacrine','Current')
retina.Connect('SNL_amacrine','tmp_bipolar','Conductance')

# Bipolar-ganglion synapse
retina.Connect('SNL_bipolar','Gauss_ganglion','Current')
retina.Connect('Gauss_ganglion','SNL_ganglion','Current')

# Connection with NEST
retina.Connect('SNL_ganglion','Output','Current')

### Displays and data analysis  ###

#retina.Show('Input','True','margin','0')
#retina.Show('SNL_photoreceptors','True','margin','0')
#retina.Show('SNL_horizontal','True','margin','0')
#retina.Show('SNL_bipolar','True','margin','0')
#retina.Show('SNL_amacrine','True','margin','0')
#retina.Show('SNL_ganglion','True','margin','0')

# Spatial multimeters of row/col 12th at 200 ms
# row selection
#retina.multimeter('spatial','Horizontal cells','SNL_horizontal',{'timeStep','200','rowcol','True','value','12'},'Show','True')
# col selection
#retina.multimeter('spatial','Horizontal cells','SNL_horizontal',{'timeStep','200','rowcol','False','value','12'},'Show','True')

# Temporal multimeter of ganglion cell at (5,5)
#retina.multimeter('temporal','Ganglion cell','SNL_ganglion',{'x','5','y','5'},'Show','True','startTime','100')

retina.multimeter('temporal','input1515','Input',{'x','15','y','15'},'Show','False','startTime','0')
retina.multimeter('temporal','ganglion1515','SNL_ganglion',{'x','15','y','15'},'Show','False','startTime','0')

retina.multimeter('temporal','input1718','Input',{'x','17','y','18'},'Show','False','startTime','0')
retina.multimeter('temporal','ganglion1718','SNL_ganglion',{'x','17','y','18'},'Show','False','startTime','0')

retina.multimeter('temporal','input1010','Input',{'x','10','y','10'},'Show','False','startTime','0')
retina.multimeter('temporal','ganglion1010','SNL_ganglion',{'x','10','y','10'},'Show','False','startTime','0')

retina.multimeter('temporal','input1212','Input',{'x','12','y','12'},'Show','False','startTime','0')
retina.multimeter('temporal','ganglion1212','SNL_ganglion',{'x','12','y','12'},'Show','False','startTime','0')

retina.multimeter('temporal','input1414','Input',{'x','14','y','14'},'Show','False','startTime','0')
retina.multimeter('temporal','ganglion1414','SNL_ganglion',{'x','14','y','14'},'Show','False','startTime','0')

retina.multimeter('temporal','input1616','Input',{'x','16','y','16'},'Show','False','startTime','0')
retina.multimeter('temporal','ganglion1616','SNL_ganglion',{'x','16','y','16'},'Show','False','startTime','0')

retina.multimeter('temporal','input1818','Input',{'x','18','y','18'},'Show','False','startTime','0')
retina.multimeter('temporal','ganglion1818','SNL_ganglion',{'x','18','y','18'},'Show','False','startTime','0')


