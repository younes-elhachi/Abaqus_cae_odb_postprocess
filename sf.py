import numpy as np
from pylab import *

numvar = 24
nvar = range(numvar)
mvar = range(numvar)

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

def schmidfactor(planes, dirs, load_dir):
	sf = []
	for i in range(len(planes)):
		sf.append( np.dot(planes[i],load_dir) * np.dot(dirs[i],load_dir) )
	return sf

sf = schmidfactor(nvar,mvar,[0,0,1])
sf = schmidfactor(nvar,mvar,[0,sqrt(2)/2,sqrt(2)/2])
sf = schmidfactor(nvar,mvar,[sqrt(3)/3,sqrt(3)/3,sqrt(3)/3])
sf = schmidfactor(nvar,mvar,[0,0.57358,0.81915])
sf = schmidfactor(nvar,mvar,[0.23329,0.52399,0.81915])
sf = schmidfactor(nvar,mvar,[0.40558,0.40558,0.81915])
sf = schmidfactor(nvar,mvar,[-0.27269314, -0.28096829,  0.92016046])

with open('sf.txt','w') as f:
	for item in sf:
		f.write('%s\n'%item)
