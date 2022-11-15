# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 01:32:52 2021

@author: Basheer
"""
import numpy as np

m=2         #"Order of Matrix"
Mat=np.zeros([m,m])
eig=np.zeros(m)
Mat[0,:]=2, 0
Mat[1,:]=0, 2
#Mat[2,:]=-2, -6, -8
eig=2,2
ee=eig[0]

def Egv(x):
    global Mat,m,ee
    L=np.zeros([m,m])
    for i in range(m):
        L[i,i]=ee
    B=Mat-L
    return np.sum(np.matmul(B,x))

def dfe(x):
    global m
    dfde=np.zeros(m)
    f1=np.zeros(m)
    f2=np.zeros(m)
    f1=Egv(x)
    for i in range(m):
        x[i]=x[i]+0.001
        f2[i]=Egv(x)
        dfde[i]=(f2[i]-f1)/0.001
    return dfde

itr=0
x=np.zeros(m)
Ch=100.0*np.ones(m)
while (np.abs(np.linalg.norm(Ch))>0.00001):
    itr=itr+1
    fx=Egv(x)
    dfx=dfe(x)
    for i in range(m):
        if (dfx[i]==0):
            x[i]=x[i]
        else:
            x[i]=x[i]-fx/dfx[i]   
    Ch=fx
    print('Iteration:',itr,'EigenValue: ',ee,'EigenVector:',x,'Error:',Ch)
        
