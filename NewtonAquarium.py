# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 18:01:54 2021

@author: Basheer
"""

import numpy as np

V=8.0
Cm=10.0
Cg=2.0

msg='Newton Aquarium'
print(msg)


def C(x):
    global V, Cm, Cg
    return x[0]*x[1]*Cm+2.0*V*(1.0/x[1]+1.0/x[0])*Cg

def F(x):
    global V, Cm, Cg
    f0=x[1]*Cm-2*V*Cg/x[0]**2
    f1=x[0]*Cm-2*V*Cg/x[1]**2
    return np.array([f0,f1])

def DF(x):
    global V, Cm, Cg
    df00=4*V*Cg/x[0]**3
    df01=Cm
    df10=Cm
    df11=4*V*Cg/x[1]**3
    return np.array([[df00,df01],[df01,df11]])

x=np.zeros(2)
f=np.zeros(2)
df=np.zeros([2,2])
invdf=np.zeros([2,2])
dx=np.ones(2)

x=[0.1,1.0]
iter=0

while np.max(np.abs(dx))>1.0e-10:
    iter=iter+1
    f=F(x)
    df=DF(x)
    print('Iter=',iter,'x=',x)
    invdf=np.linalg.inv(df)
    dx=np.matmul(invdf,-f)
    print('dx=',dx)
    x=x+dx