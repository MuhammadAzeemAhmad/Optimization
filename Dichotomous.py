# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 09:34:49 2021

@author: Basheer
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (np.exp(-0.5*x))*(np.cos(3.0*x))**2.0

msg="Dichotomous Search"
print(msg)

xl=0.4
xu=1.0
dx=0.0001
Tol=0.000001
n=50
j=0
fxa=1000.0
fxb=500.0

#for j in range(n):
while (abs(fxa-fxb)>Tol):
    j=j+1
    x=np.linspace(xl,xu,100)
    y=f(x)
    plt.plot(x,y)
    plt.show()

    print('Iteration: ',j+1)
    xm=(xl+xu)/2.0
    xa=xm-dx
    fxa=f(xa)
    xb=xm+dx
    fxb=f(xb)
    
    if (fxa<fxb):
        xu=xb
    else:
        xl=xa
        
    print('XL:',xl,'XU:',xu,'XA',xa,'fxa:',fxa,'XB',xb,'fxb',fxb)