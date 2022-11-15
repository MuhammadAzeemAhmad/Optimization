# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:38:53 2021

@author: Basheer
"""
import numpy as np
import matplotlib.pyplot as plt

msg='Steepest Descent'
print(msg)

def f(x):
    return np.exp(-0.5*x)*(np.cos(3*x))**2

def quadint(x2,df,alpha):
    alpha1=alpha-dalpha
    alpha3=alpha+dalpha
    
    x1=x2-alpha1*df
    x2=x2-alpha*df
    x3=x2-alpha3*df
    
    f1=f(x1)
    f2=f(x2)
    f3=f(x3)
    
    alpha=alpha+(((f1-f3)*dalpha)/(2*(f1-2*f2+f3)))
    return (x2,alpha)

x2=0.4
dx=0.000001
dalpha=0.01
alpha=0.1
iterations=50

for j in range(iterations):
    
    f0=f(x2)
    f1=f(x2+dx)
    df=(f1-f0)/dx
    
    (x2,alpha)=quadint(x2,df,alpha)
    a=np.linspace(x2-alpha*10,x2+alpha*10)
    b=f(a)
    plt.plot(a,b)
    plt.show()
    print(j,'x2',x2,'alpha',alpha)