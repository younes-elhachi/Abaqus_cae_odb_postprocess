from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
from odbAccess import *
import numpy as np


input = 'poly-fixed-06.odb'

inst = session.odbs[input].rootAssembly.instances['TESS-1']
keys = inst.elementSets.keys()
ndkeys = inst.nodeSets.keys()

uniqnds = []
tmplist = []
for key in keys:
    tmplist = []
    for el in inst.elementSets[key].elements:
        tmplist.extend(el.connectivity)
    uniqnds.append(np.unique(tmplist))
    
np.save('elset_nodes.npy', np.array(uniqnds))

tuniqnds = np.load('elset_nodes.npy')
tmplist = []
tmpneighors = []
for i, elset in enumerate(tuniqnds):
    tmplist = []
    for nod in elset:
        srch = [nod in nds for nds in tuniqnds]
        tmplist.extend([j for j, x in enumerate(srch) if x])
    tmpneighors.append(np.unique(tmplist))

neighors = []
for i, elset in enumerate(tmpneighors):
    index = np.argwhere(elset==i)
    neighors.append(np.delete(elset,index))
    
np.save('elset_neighbors.npy', np.array(neighors))
