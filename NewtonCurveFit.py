# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 17:14:59 2021

@author: Basheer
"""

import numpy as np
import matplotlib.pyplot as plt

def fun(x):
    global p
    return x[0]*(np.exp(p/x[1])-np.exp(-p/x[2]))

def C(x):
    global iexp,icalc
    icalc=fun(x)
    sse=np.sum((iexp-icalc)**2)
    return sse

def F(x):
    dx=1.0e-6
    ef0=C(x)
    n=np.size(x)
    f=np.zeros(n)
    for i in range(n):
        x[i]=x[i]+dx
        ef1=C(x)
        f[i]=(ef1-ef0)/dx
        x[i]=x[i]-dx
    return f

def DF(x):
    dx=1.0e-6
    n=np.size(x)
    df=np.zeros([n,n])
    f0=np.zeros(n)
    f1=np.zeros(n)
    f0=F(x)
    for i in range(n):
        x[i]=x[i]+dx
        f1=F(x)
        df[:][i]=(f1-f0)/dx
    return df

def Tame(x,DelX,f):
    n=np.size(x)
    xg=np.zeros(n)
    g=1.0
    delxmax=np.max(np.abs(DelX))
    g=2.0/delxmax
    if g>1.0:
        g=1.0
    return g

print('Newton CurveFit')

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
iexp=fun([iexp,baexp,bcexp])
f=np.ones(n)
df=np.zeros([n,n])
dfinv=np.zeros([n,n])
DelX=np.zeros(n)

x=[50.0, 50.0, 50.0]
g=0.01

iter=0
while np.max(np.abs(f))>1.0e-5:
    iter=iter+1
    f=F(x)
    print('iter',iter,'f',f)
    print('x',x)
    df=DF(x)
    dfinv=np.linalg.inv(df)
    DelX=np.matmul(dfinv,-f)
    #g=Tame(x,DelX,f)
    for j in range(n):
        x[j]=x[j]+g*DelX[j]
        