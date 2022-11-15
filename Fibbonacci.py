# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 09:39:55 2021

@author: 
"""

import numpy as np
import matplotlib.pyplot as plt
from array import *

def f(x):
    return 1/4*x**4-5/3*x**3-6*x**2+19*x-7

msg="Fibbonacci Search"
print(msg)

xl=-4.0
xu=0.0
n=20
i=0

F=array('d',[1,1])
for j in range(n-2):
    F.append(F[j+1]+F[j])
    
I=array('d',[xu-xl])    
for j in range(n-1):
    i=n-j-2
    #print(i)
    #print(i-1)
    I.append(I[j]*F[i]/F[i+1])
    
xa=xu-I[1]
xb=xl+I[1]
fa=f(xa)
fb=f(xb)
#print(F)
#print(I)
for j in range(n-2):
    x=np.linspace(xl,xu,100)
    y=f(x)
    #plt.clear()
    plt.close()
    plt.plot(x,y)
    plt.show()
    
    print('Iteration: ',j)
    print('XL:',xl,'XU:',xu,'XA',xa,'fxa:',fa,'XB',xb,'fxb',fb)


    if (fb<fa):
        xl=xa
        xa=xb
        fa=fb
        xb=xl+I[j+2]
        fb=f(xb)
    else:
        xu=xb
        xb=xa
        fb=fa
        xa=xu-I[j+2]
        fa=f(xa)
    txt=input('Next iteration?')