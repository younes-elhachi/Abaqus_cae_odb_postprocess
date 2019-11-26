# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-5 replay file
# Internal Version: 2015_08_18-16.32.57 135153
# Run by elhachi on Fri Oct 11 14:26:20 2019
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
#: Executing "onCaeGraphicsStartup()" in the local directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=130.110931396484, 
    height=191.076171875)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)

list_odb = ['Job-100.odb',
            'Job-110.odb',
            'Job-T1.odb',
            'Job-or1.odb',
            'Job-or2.odb',
            'Job-or3.odb']

list_odb = ['grain-vert.odb',
            'grain-bleu.odb',
            'grain-rouge.odb',
            'grain-noir.odb']
for odbf in list_odb:
	o1 = session.openOdb(
		name=odbf)
	session.viewports['Viewport: 1'].setValues(displayedObject=o1)
	odb = session.odbs[odbf]
	session.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
		variable=(('E', INTEGRATION_POINT, ((COMPONENT, 'E11'), (COMPONENT, 'E22'), 
		(COMPONENT, 'E33'), (COMPONENT, 'E12'), (COMPONENT, 'E13'), (COMPONENT, 
		'E23'), )), ('S', INTEGRATION_POINT, ((INVARIANT, 'Mises'), (COMPONENT, 
		'S11'), (COMPONENT, 'S22'), (COMPONENT, 'S33'), (COMPONENT, 'S12'), (
		COMPONENT, 'S13'), (COMPONENT, 'S23'), )), ), elementSets=(' ALL ELEMENTS', 
		))
	for i in range(1,37):
		session.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
			variable=(('SDV%d'%i, INTEGRATION_POINT), ), elementSets=(
			' ALL ELEMENTS', ))
		
	x0 = session.xyDataObjects['E:E11 PI: CUBE-1 E: 1 IP: 1']
	x1 = session.xyDataObjects['E:E22 PI: CUBE-1 E: 1 IP: 1']
	x2 = session.xyDataObjects['E:E33 PI: CUBE-1 E: 1 IP: 1']
	x3 = session.xyDataObjects['E:E12 PI: CUBE-1 E: 1 IP: 1']
	x4 = session.xyDataObjects['E:E13 PI: CUBE-1 E: 1 IP: 1']
	x5 = session.xyDataObjects['E:E23 PI: CUBE-1 E: 1 IP: 1']

	x6 = session.xyDataObjects['S:S11 PI: CUBE-1 E: 1 IP: 1']
	x7 = session.xyDataObjects['S:S22 PI: CUBE-1 E: 1 IP: 1']
	x8 = session.xyDataObjects['S:S33 PI: CUBE-1 E: 1 IP: 1']
	x9 = session.xyDataObjects['S:S12 PI: CUBE-1 E: 1 IP: 1']
	x10 = session.xyDataObjects['S:S13 PI: CUBE-1 E: 1 IP: 1']
	x11 = session.xyDataObjects['S:S23 PI: CUBE-1 E: 1 IP: 1']
	x12 = session.xyDataObjects['S:Mises PI: CUBE-1 E: 1 IP: 1']

	x13 = session.xyDataObjects['SDV6 PI: CUBE-1 E: 1 IP: 1']
	x14 = session.xyDataObjects['SDV7 PI: CUBE-1 E: 1 IP: 1']
	x15 = session.xyDataObjects['SDV8 PI: CUBE-1 E: 1 IP: 1']
	x16 = session.xyDataObjects['SDV9 PI: CUBE-1 E: 1 IP: 1']
	x17 = session.xyDataObjects['SDV10 PI: CUBE-1 E: 1 IP: 1']
	x18 = session.xyDataObjects['SDV11 PI: CUBE-1 E: 1 IP: 1']
	x19 = session.xyDataObjects['SDV12 PI: CUBE-1 E: 1 IP: 1']
	x20 = session.xyDataObjects['SDV13 PI: CUBE-1 E: 1 IP: 1']
	x21 = session.xyDataObjects['SDV14 PI: CUBE-1 E: 1 IP: 1']
	x22 = session.xyDataObjects['SDV15 PI: CUBE-1 E: 1 IP: 1']
	x23 = session.xyDataObjects['SDV16 PI: CUBE-1 E: 1 IP: 1']
	x24 = session.xyDataObjects['SDV17 PI: CUBE-1 E: 1 IP: 1']
	x25 = session.xyDataObjects['SDV18 PI: CUBE-1 E: 1 IP: 1']
	x26 = session.xyDataObjects['SDV19 PI: CUBE-1 E: 1 IP: 1']
	x27 = session.xyDataObjects['SDV20 PI: CUBE-1 E: 1 IP: 1']
	x28 = session.xyDataObjects['SDV21 PI: CUBE-1 E: 1 IP: 1']
	x29 = session.xyDataObjects['SDV22 PI: CUBE-1 E: 1 IP: 1']
	x30 = session.xyDataObjects['SDV23 PI: CUBE-1 E: 1 IP: 1']
	x31 = session.xyDataObjects['SDV24 PI: CUBE-1 E: 1 IP: 1']
	x32 = session.xyDataObjects['SDV25 PI: CUBE-1 E: 1 IP: 1']
	x33 = session.xyDataObjects['SDV26 PI: CUBE-1 E: 1 IP: 1']
	x34 = session.xyDataObjects['SDV27 PI: CUBE-1 E: 1 IP: 1']
	x35 = session.xyDataObjects['SDV28 PI: CUBE-1 E: 1 IP: 1']
	x36 = session.xyDataObjects['SDV29 PI: CUBE-1 E: 1 IP: 1']
	x37 = session.xyDataObjects['SDV36 PI: CUBE-1 E: 1 IP: 1']

	alldata = (x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36,x37)
	session.writeXYReport(fileName='%sdata.rpt'%odbf[:-4], appendMode=OFF, xyData=alldata)
	for item in session.xyDataObjects.keys():
		del session.xyDataObjects[item]
