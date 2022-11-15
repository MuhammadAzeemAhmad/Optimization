# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 20:30:12 2021

@author: Basheer
"""

"Eigen Value Calculator"

import numpy as np

m=2         #"Order of Matrix"
Mat=np.zeros([m,m])
Mat[0,:]=2, 0
Mat[1,:]=0, 2
#Mat[2,:]=-2, -6, -8


def f(x):
    global Mat, m
    L=np.zeros([m,m])
    for i in range(m):
        L[i,i]=x[i]
    B=Mat-L
    return np.linalg.det(B**2)
    #return B

def df(x):
    global m
    dfdx=np.zeros(m)
    f1=np.zeros(m)
    f2=np.zeros(m)
    f1=f(x)
    for i in range(m):
        x[i]=x[i]+0.001
        f2[i]=f(x)
        dfdx[i]=(f2[i]-f1)/0.001
    return dfdx



itr=0
Ch=1000
eig=np.ones(m)

while (np.abs(Ch)>0.00001):
    itr=itr+1
    fx=f(eig)
    dfx=df(eig)
    for i in range(m):
        if (dfx[i]==0):
            eig[i]=eig[i]
        else:
            eig[i]=eig[i]-fx/dfx[i]
#        Prod=np.matmul(Mat,eig)
#        eig[i]=(Prod[i])/np.linalg.norm(Prod)
    #Prod=np.matmul(np.linalg.inv(fx),eig)
    #eig=Prod
    Ch=fx
    print('Iteration:',itr,'EigenValues: ',eig,'Error:',Ch)

