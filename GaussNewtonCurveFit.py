# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 20:19:54 2021

@author: Basheer
"""


import numpy as np
import matplotlib.pyplot as plt

def fun(x):
    global p
    return x[0]*(np.exp(p/x[1])-np.exp(-p/x[2]))

def R(x):
    global iexp, icalc
    ecalc=fun(x)
    return icalc-iexp

def JR(x):
    global ndata, n
    r1=np.zeros(ndata)
    r2=np.zeros(ndata)
    jr=np.zeros([ndata,n])
    r1=R(x)
    dx=1.0e-6
    for j in range(n):
        xtemp=x[j]
        x[j]=x[j]+dx
        r2=R(x)
        x[j]=xtemp
        for i in range(ndata):
            jr[i][j]=(r2[i]-r1[i])/dx
    return jr

def Tame(DelX):
    g=1.0
    delxmax=np.max(np.abs(DelX))
    g=2.0/delxmax
    return g

print('Gauss-Newton CurveFit')

ndata=21
n=3
pmin=-100.0
pmax=100.0
icexp=100.0
baexp=100.0
bcexp=200.0
p=np.linspace(pmin,pmax,ndata)
iexp=np.zeros(ndata)
icalc=np.zeros(ndata)
r=np.zeros(ndata)
Jr=np.zeros([ndata,n])
JrT=np.zeros([ndata,n])
iexp=fun([iexp,baexp,bcexp])
f=np.zeros(n)
df=np.zeros([n,n])
dfinv=np.zeros([n,n])
DelX=np.zeros(n)

x=[50.0, 50.0, 50.0]
g=1.0
Delx=10.0
iter=0
while (np.abs(Delx)>1.0e-10):
    iter=iter+1
    print('iter=',iter,'x=',x)
    r=R(x)
    Jr=JR(x)
    JrT=np.transpose(Jr)
    Delx=-np.matmul(np.matmul(np.linalg.inv(np.matmul(JrT,Jr)),JrT),r)
    x=x+Delx
