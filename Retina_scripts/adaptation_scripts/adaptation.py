retina.TempStep('1')
retina.SimTime('15000')
retina.NumTrials('1')
retina.PixelsPerDegree({'5'})
retina.DisplayDelay('0')
retina.DisplayZoom({'10.0'})
retina.DisplayWindows('3')
retina.Input('sequence','input_sequences/Weberlaw/HMM_sequence/',{'InputFramePeriod','50'})
retina.Create('LinearFilter','tmp_tauR',{'type','Gamma','tau','0.49','n','0.0'})
retina.Create('LinearFilter','tmp_tauE',{'type','Gamma','tau','16.8','n','0.0'})
retina.Create('SingleCompartment','calcium_feedback_SC',{'number_current_ports','1.0','number_conductance_ports','2.0','Rm','0.0','Cm','1.0','E',{'0.0','0.0'}})
retina.Create('LinearFilter','tmp_tauC',{'type','Gamma','tau','2.89','n','0.0'})
retina.Create('LinearFilter','tmp_taum',{'type','Gamma','tau','4.0','n','0.0'})
retina.Create('LinearFilter','tmp_tauis',{'type','Gamma','tau','56.9','n','0.0'})
retina.Create('LinearFilter','tmp_tau1',{'type','Gamma','tau','4.0','n','0.0'})
retina.Create('LinearFilter','tmp_tau2',{'type','Gamma','tau','4.0','n','0.0'})
retina.Create('LinearFilter','tmp_tauh',{'type','Gamma','tau','20.0','n','0.0'})
retina.Create('StaticNonLinearity','beta',{'slope','0.000163','offset','0.0028','exponent','1.0'})
retina.Create('StaticNonLinearity','X',{'slope','1.0','offset','0.0','exponent','1.0'})
retina.Create('StaticNonLinearity','1_div_alpha',{'slope','0.0908','offset','1.0','exponent','4.0'})
retina.Create('StaticNonLinearity','alpha',{'slope','1.0','offset','0.0001','exponent','-1.0'})
retina.Create('StaticNonLinearity','ais',{'slope','0.0709','offset','0.0','exponent','0.678'})
retina.Create('StaticNonLinearity','Vis',{'slope','1.0','offset','-13.9','exponent','1.0'})
retina.Create('StaticNonLinearity','gs',{'slope','0.5','offset','0.0','exponent','1.0'})
retina.Connect('L_cones','tmp_tauR','Current')
retina.Connect('tmp_tauR','tmp_tauE','Current')
retina.Connect('tmp_tauE','beta','Current')
retina.Connect('alpha','calcium_feedback_SC','Current')
retina.Connect('beta','calcium_feedback_SC','Conductance')
retina.Connect('calcium_feedback_SC','X','Current')
retina.Connect('X','tmp_tauC','Current')
retina.Connect('tmp_tauC','1_div_alpha','Current')
retina.Connect('1_div_alpha','alpha','Current')
retina.Connect({'X',/,'tmp_tauis'},'tmp_taum','Current')
retina.Connect('tmp_taum','ais','Current')
retina.Connect('ais','tmp_tauis','Current')
retina.Connect('tmp_taum','Vis','Current')
retina.Connect({'Vis',-,'tmp_tauh'},'gs','Current')
retina.Connect('gs','tmp_tau1','Current')
retina.Connect('tmp_tau1','tmp_tau2','Current')
retina.Connect('tmp_tau2','tmp_tauh','Current')
retina.Show('X','True','margin','0')
retina.Show('gs','True','margin','0')
retina.Show('tmp_tau1','True','margin','0')
retina.multimeter('temporal','Vis1010','Vis',{'x','10','y','10'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1011','Vis',{'x','10','y','11'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1012','Vis',{'x','10','y','12'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1013','Vis',{'x','10','y','13'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1014','Vis',{'x','10','y','14'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1015','Vis',{'x','10','y','15'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1016','Vis',{'x','10','y','16'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1017','Vis',{'x','10','y','17'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1018','Vis',{'x','10','y','18'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1019','Vis',{'x','10','y','19'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1020','Vis',{'x','10','y','20'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1110','Vis',{'x','11','y','10'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1111','Vis',{'x','11','y','11'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1112','Vis',{'x','11','y','12'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1113','Vis',{'x','11','y','13'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1114','Vis',{'x','11','y','14'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1115','Vis',{'x','11','y','15'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1116','Vis',{'x','11','y','16'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1117','Vis',{'x','11','y','17'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1118','Vis',{'x','11','y','18'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1119','Vis',{'x','11','y','19'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1120','Vis',{'x','11','y','20'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1210','Vis',{'x','12','y','10'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1211','Vis',{'x','12','y','11'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1212','Vis',{'x','12','y','12'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1213','Vis',{'x','12','y','13'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1214','Vis',{'x','12','y','14'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1215','Vis',{'x','12','y','15'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1216','Vis',{'x','12','y','16'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1217','Vis',{'x','12','y','17'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1218','Vis',{'x','12','y','18'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1219','Vis',{'x','12','y','19'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1220','Vis',{'x','12','y','20'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1310','Vis',{'x','13','y','10'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1311','Vis',{'x','13','y','11'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1312','Vis',{'x','13','y','12'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1313','Vis',{'x','13','y','13'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1314','Vis',{'x','13','y','14'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1315','Vis',{'x','13','y','15'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1316','Vis',{'x','13','y','16'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1317','Vis',{'x','13','y','17'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1318','Vis',{'x','13','y','18'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1319','Vis',{'x','13','y','19'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1320','Vis',{'x','13','y','20'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1410','Vis',{'x','14','y','10'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1411','Vis',{'x','14','y','11'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1412','Vis',{'x','14','y','12'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1413','Vis',{'x','14','y','13'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1414','Vis',{'x','14','y','14'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1415','Vis',{'x','14','y','15'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1416','Vis',{'x','14','y','16'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1417','Vis',{'x','14','y','17'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1418','Vis',{'x','14','y','18'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1419','Vis',{'x','14','y','19'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1420','Vis',{'x','14','y','20'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1510','Vis',{'x','15','y','10'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1511','Vis',{'x','15','y','11'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1512','Vis',{'x','15','y','12'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1513','Vis',{'x','15','y','13'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1514','Vis',{'x','15','y','14'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1515','Vis',{'x','15','y','15'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1516','Vis',{'x','15','y','16'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1517','Vis',{'x','15','y','17'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1518','Vis',{'x','15','y','18'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1519','Vis',{'x','15','y','19'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1520','Vis',{'x','15','y','20'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1610','Vis',{'x','16','y','10'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1611','Vis',{'x','16','y','11'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1612','Vis',{'x','16','y','12'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1613','Vis',{'x','16','y','13'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1614','Vis',{'x','16','y','14'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1615','Vis',{'x','16','y','15'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1616','Vis',{'x','16','y','16'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1617','Vis',{'x','16','y','17'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1618','Vis',{'x','16','y','18'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1619','Vis',{'x','16','y','19'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1620','Vis',{'x','16','y','20'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1710','Vis',{'x','17','y','10'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1711','Vis',{'x','17','y','11'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1712','Vis',{'x','17','y','12'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1713','Vis',{'x','17','y','13'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1714','Vis',{'x','17','y','14'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1715','Vis',{'x','17','y','15'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1716','Vis',{'x','17','y','16'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1717','Vis',{'x','17','y','17'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1718','Vis',{'x','17','y','18'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1719','Vis',{'x','17','y','19'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1720','Vis',{'x','17','y','20'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1810','Vis',{'x','18','y','10'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1811','Vis',{'x','18','y','11'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1812','Vis',{'x','18','y','12'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1813','Vis',{'x','18','y','13'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1814','Vis',{'x','18','y','14'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1815','Vis',{'x','18','y','15'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1816','Vis',{'x','18','y','16'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1817','Vis',{'x','18','y','17'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1818','Vis',{'x','18','y','18'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1819','Vis',{'x','18','y','19'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1820','Vis',{'x','18','y','20'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1910','Vis',{'x','19','y','10'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1911','Vis',{'x','19','y','11'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1912','Vis',{'x','19','y','12'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1913','Vis',{'x','19','y','13'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1914','Vis',{'x','19','y','14'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1915','Vis',{'x','19','y','15'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1916','Vis',{'x','19','y','16'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1917','Vis',{'x','19','y','17'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1918','Vis',{'x','19','y','18'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1919','Vis',{'x','19','y','19'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis1920','Vis',{'x','19','y','20'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis2010','Vis',{'x','20','y','10'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis2011','Vis',{'x','20','y','11'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis2012','Vis',{'x','20','y','12'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis2013','Vis',{'x','20','y','13'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis2014','Vis',{'x','20','y','14'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis2015','Vis',{'x','20','y','15'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis2016','Vis',{'x','20','y','16'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis2017','Vis',{'x','20','y','17'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis2018','Vis',{'x','20','y','18'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis2019','Vis',{'x','20','y','19'},'Show','False','startTime','0')
retina.multimeter('temporal','Vis2020','Vis',{'x','20','y','20'},'Show','False','startTime','0')
