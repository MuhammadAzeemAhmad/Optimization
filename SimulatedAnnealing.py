# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 14:48:07 2021

@author: Basheer
"""

import random as rn
import numpy as np
import matplotlib.pyplot as plt


msg='Simulated Annealing'
print(msg)

def fun(x):
    return np.exp(-3.0*x)*np.sin(15.0*x)

def Xnew(x):
    s=0.01
    r=rn.random()
    #r=rn.rand()
    x=x+s*x*(r-0.5)
    return x

Tmax=100.0
Tmin=1.0e-5
TR=0.98
Nsteps=50
x=0.5
C=fun(x)
xmin=x
Cmin=C
xaxis=np.linspace(0,1,100)
yaxis=fun(xaxis)
plt.plot(xaxis,yaxis)
T=Tmax

iter=0

while (T>Tmin):
    iter=iter+1
    print('iter=',iter,'xmin=',xmin,'Cost=',Cmin,'T=',T)
    jstep=0
    while (jstep<Nsteps):
        jstep=jstep+1
        x=Xnew(x)
        #print(x)
        C=fun(x)
        #print(C)
        
        dC=C-Cmin
        
        #if dC<0:
        if C<Cmin:
            xmin=x
            Cmin=C
        else:
            p=np.exp(-dC/T)
            r=rn.random()
            if p>0.5:
                xmin=x
                Cmin=C
            else:
                xmin=xmin
                Cmin=Cmin
            
    T=T*TR
    
    