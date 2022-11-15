# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 07:59:58 2021

@author: Basheer
"""
import numpy as np

V=8.0
Cm=10.0
Cg=2.0

msg='Multivariable Steepest Descent'
print(msg)


def C(x):
    global V, Cm, Cg
    return x[0]*x[1]*Cm+2.0*V*(1.0/x[1]+1.0/x[0])*Cg

def DF(x):
    df0=x[1]*Cm-2*V*Cg/x[0]**2
    df1=x[0]*Cm-2*V*Cg/x[1]**2
    return [df0, df1]
    
def Quad(x):
    x1=[0.0,0.0]
    x2=[0.0,0.0]
    x3=[0.0,0.0]
    dx=1.0e-6
    dg=1.0e-3
    g2=1.0e-2
    g1=g2-dg
    g3=g2+dg
    df=DF(x0)
    x1[0]=x0[0]-g1*df[0]
    x1[1]=x0[1]-g1*df[1]
    x2[0]=x0[0]-g2*df[0]
    x2[1]=x0[1]-g2*df[1]
    x3[0]=x0[0]-g3*df[0]
    x3[1]=x0[1]-g3*df[1]
    
    f1=C(x1)
    f2=C(x2)
    f3=C(x3)
    
    g=g2+(f1-f3)*dg/2/(f1-2*f2+f3)
    if g<0.0:
        g=1.0e-5
    return [g,df]

def Tame(x0):
    n=np.size(x0)
    f0=C(x0)
    df=np.zeros(n)
    df=DF(x0)
    x=np.zeros(n)
    dd=0.0
    g=1.0
    #for i in range(n):
     #   dd=dd+np.abs(f0/df[i]**2)
    #g=float(dd/n)
    
    iter=0
    while iter<50:
        iter=iter+1
        for i in range(n):
            x[i]=x0[i]-g*df[i]
        f=C(x)
    if f>f0 or min(x)<0.0:
        g=g/2.0
    
    if f>f0:
        g,df=Quad(x0)
    return g
        
    

x0=[1.0, 2.0]
f0=C(x0)
df=DF(x0)
g=5.0e-2
print(f0,df)
fold=1.0e99
iter=0

while np.abs(f0-fold)>1.0e-10:
    fold=f0
    print('iter',iter,'g',g,'f',f0)
    print('x0',x0[0],'x1',x0[1])
    iter=iter+1
    #g,df=Quad(x0)
    g=Tame(x0)
    df=DF(x0)
    x0[0]=x0[0]-g*df[0]
    x0[1]=x0[1]-g*df[1]
    f0=C(x0)
    
    
    
    
    
    