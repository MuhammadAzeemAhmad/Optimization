# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 15:27:02 2021

@author: Basheer
"""
import numpy as np
import matplotlib.pyplot as plt

msg='Quadratic Interpolation'
print(msg)

def f(x):
    return np.exp(-0.5*x)*(np.cos(3*x))**2

x0=10.0
xbar=20.0
fbar=f(xbar)
x1=0.4
x3=1.0
Tol=0.000001
n=50
x2=0.5*(x1+x3)
f1=f(x1)
f2=f(x2)
f3=f(x3)
iterr=0
print('X1:',x1,'X2:',x2,'X3',x3,'Xbar',xbar,'fbar',fbar,'X0',x0)
#for j in range(n):
while (abs(x0-xbar)>=Tol):
    a=np.linspace(x1,x3)
    b=f(a)
    plt.plot(a,b)
    plt.show()
    iterr=iterr+1
    print('Iteration: ',iterr)
    num=((x2**2.0-x3**2.0)*f1)+((x3**2.0-x1**2.0)*f2)+((x1**2.0-x2**2.0)*f3)
    den=2.0*(((x2-x3)*f1)+((x3-x1)*f2)+((x1-x2)*f3))
    x0=xbar
    xbar=num/den
    fbar=f(xbar)
    print('X1:',x1,'X2:',x2,'X3',x3,'Xbar',xbar,'fbar',fbar,'X0',x0)
    if (x1<xbar<x2):
        if (fbar<=f2):
            x3=x2
            f3=f2
            x2=xbar
            f2=fbar
        elif (fbar>f2):
            x1=xbar
            f1=fbar
            
    if (x2<xbar<x3):
        if (fbar<=f2):
            x1=x2
            f1=f2
            x2=xbar
            f2=fbar
        elif (fbar>f2):
            x3=xbar
            f3=fbar
            
    