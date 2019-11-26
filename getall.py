from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
from odbAccess import *
import numpy as np
import collections

numvar = 24
nvar = range(numvar)
mvar = range(numvar)
schmidvar = range(numvar)

a = -0.168
b = 0.688
c = 0.705
d = -0.121
e = 0.725
f = 0.678

nvar[0] = np.array([a,b,c])
nvar[1] = np.array([a,c,b])
nvar[2] = np.array([-a,b,c])
nvar[3] = np.array([-a,c,b])
nvar[4] = np.array([-b,a,c])
nvar[5] = np.array([-c,a,b])
nvar[6] = np.array([-b,-a,c])
nvar[7] = np.array([-c,-a,b])
nvar[8] = np.array([a,-b,c])
nvar[9] = np.array([a,-c,b])
nvar[10] = np.array([-a,-b,c])
nvar[11] = np.array([-a,-c,b])
nvar[12] = np.array([c,a,b])
nvar[13] = np.array([b,a,c])
nvar[14] = np.array([c,-a,b])
nvar[15] = np.array([b,-a,c])
nvar[16] = np.array([b,-c,-a])
nvar[17] = np.array([c,-b,-a])
nvar[18] = np.array([-b,c,-a])
nvar[19] = np.array([-c,b,-a])
nvar[20] = np.array([-c,-b,-a])
nvar[21] = np.array([-b,-c,-a])
nvar[22] = np.array([c,b,-a])
nvar[23] = np.array([b,c,-a])

mvar[0] = np.array([d,-e,f])
mvar[1] = np.array([d,f,-e])
mvar[2] = np.array([-d,-e,f])
mvar[3] = np.array([-d,f,-e])
mvar[4] = np.array([e,d,f])
mvar[5] = np.array([-f,d,-e])
mvar[6] = np.array([e,-d,f])
mvar[7] = np.array([-f,-d,-e])
mvar[8] = np.array([d,e,f])
mvar[9] = np.array([d,-f,-e])
mvar[10] = np.array([-d,e,f])
mvar[11] = np.array([-d,-f,-e])
mvar[12] = np.array([f,d,-e])
mvar[13] = np.array([-e,d,f])
mvar[14] = np.array([f,-d,-e])
mvar[15] = np.array([-e,-d,f])
mvar[16] = np.array([-e,-f,-d])
mvar[17] = np.array([f,e,-d])
mvar[18] = np.array([e,f,-d])
mvar[19] = np.array([-f,-e,-d])
mvar[20] = np.array([-f,e,-d])
mvar[21] = np.array([e,-f,-d])
mvar[22] = np.array([f,-e,-d])
mvar[23] = np.array([-e,f,-d])

for i in range (numvar):
	ni = nvar[i].reshape(3,1)
	mj = mvar[i].reshape(1,3)
	mi = mvar[i].reshape(3,1)
	nj = nvar[i].reshape(1,3)
	schmidvar[i]=.5*(np.dot(ni,mj) + np.dot(mi,nj))


def schmidfactor(planes, dirs, load_dir):
	sf = []
	for i in range(len(planes)):
		sf.append( np.dot(planes[i],load_dir) * np.dot(dirs[i],load_dir) )
	return sf

def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable):
            for sub in flatten(el):
                yield sub
        else:
            yield el

input = 'poly-fixed-06.odb'
output = 'poly-fixed-06.txt'
o1 = session.openOdb(name=input)
odb = session.odbs[input]

step1 = odb.steps['Step-1']
keys = session.odbs[input].rootAssembly.instances['TESS-1'].elementSets.keys()
nel = len(keys)
nvariables = 72
lastframe = 199
incframe = 7
idframes = np.arange(1, lastframe, incframe)
outcsys = odb.rootAssembly.datumCsyses['CSYS-1']

with open(output,'w') as outfile:
	outfile.write('# (frames, grains, variables) : (%d, %d, %d)\n'%(len(idframes), nel, nvariables))
	outfile.write('# Time E11 E22 E33 E12 E13 E23 ')
	outfile.write('S11 S22 S33 S12 S13 S23 Mises ')
	outfile.write('Mfrac frac1 frac2 frac3 frac4 frac5 frac6 frac7 frac8 frac9 ')
	outfile.write('frac10 frac11 frac12 frac13 frac14 frac15 frac16 frac17 ')
	outfile.write('frac18 frac19 frac20 frac21 frac22 frac23 frac24 ')
	outfile.write('or11 or12 or13 or21 or22 or23 or31 or32 or33 ')
	outfile.write('sf1 sf2 sf3 sf4 sf5 sf6 sf7 sf8 sf9 sf10 sf11 sf12 sf13 ')
	outfile.write('sf14 sf15 sf16 sf17 sf18 sf19 sf20 sf21 sf22 sf23 sf24 ')
	outfile.write('rss1 rss2 rss3 rss4 rss5 rss6 rss7 rss8 rss9 ')
	outfile.write('rss10 rss11 rss12 rss13 rss14 rss15 rss16 rss17 ')
	outfile.write('rss18 rss19 rss20 rss21 rss22 rss23 rss24\n')
	for inc in idframes:
		frm = step1.frames[inc]
		print 'Frame %d/%d'%((frm.frameId-1)/7+1,len(idframes))
		outfile.write('# Frame %d\n'%frm.frameId)
		frame_data = []
		for key in keys:
			elements = odb.rootAssembly.instances['TESS-1'].elementSets[key]
			E = frm.fieldOutputs['E'].getTransformedField(outcsys).getSubset(region=elements).values
			mE = np.mean([x.data for x in E], axis=0)
			S = frm.fieldOutputs['S'].getTransformedField(outcsys).getSubset(region=elements).values
			mS = np.mean([x.data for x in S], axis=0)
			mMises = np.mean([x.mises for x in S], axis=0)
			SDV36 = frm.fieldOutputs['SDV36'].getSubset(region=elements).values
			mSDV36 = np.mean([x.data for x in SDV36], axis=0)
			fracs=[frm.fieldOutputs['SDV%d'%i].getSubset(region=elements).values for i in range(6,30)]
			mFRACS = np.array([np.mean([x.data for x in f]) for f in fracs])
			ori = frm.fieldOutputs['S'].getSubset(region=elements).values[0].localCoordSystem
			orientation = np.array(ori).ravel()
			sf = schmidfactor(nvar,mvar,[orientation[2],orientation[5],orientation[8]])
			a1 = [mS[0],mS[3],mS[4]]
			a2 = [mS[3],mS[1],mS[5]]
			a3 = [mS[4],mS[5],mS[2]]
			sig = np.array([a1,a2,a3])
			mRSS = np.array([sum(np.multiply(schmidvar[x],sig)) for x in range(24)]))
			el_data = []
			el_data.append([frm.frameValue, mE, mS, mMises, mSDV36, mFRACS, orientation, sf, mRSS])
			frame_data.append([x for x in flatten(el_data)])
		np.savetxt(outfile, np.array(frame_data), fmt='%-15.8f')
