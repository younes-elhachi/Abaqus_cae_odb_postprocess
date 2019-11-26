# coding: utf-8
from pylab import *
import numpy as np
o6 = np.loadtxt('poly-fixed-06.txt').reshape(29,187,72)
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

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

tsf = np.array([schmidfactor(nvar,mvar,[o6[28,i,41],o6[28,i,44],o6[28,i,47]]) for i in range(187)])
    
cooripf = []
for i in range(187):
    [u,v,w] = sorted([float(abs(o6[28,i,j])) for j in range(45,48)])
    cooripf.append([v/(1+w),u/(1+w)])

uvws = []
for j, coo in enumerate(cooripf):
    mx,my = coo
    for mu in range(1,1000):
        fuvw = np.array([mu,mu*mx/my,mu/my-1])
        iuvw = np.array([int(round(x)) for x in fuvw])
        if sqrt(sum((fuvw-iuvw)*(fuvw-iuvw)))<0.201:
            mgcd = reduce(lambda x,y: GCD(x,y),iuvw)
            uvws.append(iuvw/mgcd)
            break

for gr in range(187):
    figure(figsize=(16,9))
    subplot(231)
    scatter(tsf[gr],o6[28,gr,15:39]*100,s=25,edgecolors='r',facecolors='none')
    xlim(-0.5,0.5)
    ylim(0,6)
    gca().set_xticks( np.arange(-0.5, 0.51, 0.2))
    gca().set_xticks( np.arange(-0.5, 0.51, 0.05), minor=True)
    gca().set_yticks( np.arange(0., 6.1, 1))
    gca().set_yticks( np.arange(0., 6.1, 0.25), minor=True)
    grid(which='major', alpha=0.5)
    grid(which='minor', alpha=0.2)
    xlabel(r'$Schmid \, factor$')
    ylabel(r'$Martensite \, variants \, (\%)$')
    
    subplot(234)
    scatter(tsf[gr],o6[28,gr,15:39]/o6[28,gr,14]*100,s=25,edgecolors='r',facecolors='none')
    xlim(-0.5,0.5)
    ylim(0,60)
    gca().set_xticks( np.arange(-0.5, 0.51, 0.2))
    gca().set_xticks( np.arange(-0.5, 0.51, 0.05), minor=True)
    gca().set_yticks( np.arange(0., 60.1, 10))
    gca().set_yticks( np.arange(0., 60.1, 2.5), minor=True)
    grid(which='major', alpha=0.5)
    grid(which='minor', alpha=0.2)
    xlabel(r'$Schmid \, factor$')
    ylabel(r'$Martensite \, variants \, (normalised) \, (\%)$')
    
    subplot(235)
    for i in range(187):
        plot(o6[:,i,14]*100,o6[:,i,3]*100,'b--',dashes=(2,2),lw=0.8,alpha=0.4)    
    xlim(0,15)
    ylim(0,0.6)
    plot(o6[:,gr,14]*100,o6[:,gr,3]*100,'r',lw=2)
    xlabel(r'$Martensite \, (\%)$')
    ylabel(r'$\varepsilon_{33} \, (\%)$')

    subplot(232)
    for i in range(187):
        plot(o6[:,i,14]*100,o6[:,i,13],'b--',dashes=(2,2),lw=0.8,alpha=0.4)    
    xlim(0,15)
    ylim(-10,240)
    plot(o6[:,gr,14]*100,o6[:,gr,13],'r',lw=2)
    xlabel(r'$Martensite \, (\%)$')
    ylabel(r'$\sigma_{mises} \, (MPa)$')    

    subplot(233)
    for i in range(187):
        plot(o6[:,i,3]*100,o6[:,i,9],'b--',dashes=(2,2),lw=0.8,alpha=0.4)    
    xlim(0,0.6)
    ylim(-10,240)
    plot(o6[:,gr,3]*100,o6[:,gr,9],'r',lw=2)
    xlabel(r'$\varepsilon_{33} \, (\%)$')
    ylabel(r'$\sigma_{33} \, (MPa)$')

    subplot(236)
    scatter([x[0] for x in cooripf],[x[1] for x in cooripf],marker='x',lw=0.8,alpha=0.6)
    axis('off')
    gca().set_aspect('equal')
    annotate('[0 0 1]',xy=(0.25,0.25),xytext=(-0.01,0.))
    annotate('[1 1 1]',xy=(0.25,0.25),xytext=(0.36,0.36))
    annotate('[0 1 1]',xy=(0.25,0.25),xytext=(0.42,0.))
    scatter(cooripf[gr][0],cooripf[gr][1],marker='x',color='red',lw=1.5)
    u1,v1,w1 = uvws[gr]
    annotate('[%d %d %d]'%(u1,v1,w1),xy=(cooripf[gr]),xytext=(0.11,0.22),color='red',arrowprops=dict(color='red',width=0.4,headwidth=5,shrink=0.04,headlength=5))
    
    gcf().suptitle(r'$Grain \, %d$'%gr)
    gcf().tight_layout()
    savefig('plots/grain_%03d.png'%gr,dpi=300)

