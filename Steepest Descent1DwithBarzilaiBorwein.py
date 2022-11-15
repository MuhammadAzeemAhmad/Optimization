# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 08:28:36 2021

@author: Basheer
"""

import numpy as np
import matplotlib.pyplot as plt

msg='Steepest Descent Barzilai-Borwein Method'
print(msg)

def f(x):
    return np.exp(-0.5*x)*(np.cos(3*x))**2

x0=0.4
dx=0.000001
dalpha=0.01
alpha=0.1
iterations=50

for j in range(iterations):
    
    x1=x0+dx
    x2=x1+dx
    
    df2=(f(x2)-f(x1))/dx
    df1=(f(x1)-f(x0))/dx
    
    alpha=((x2-x1)*(df2-df1))/((df2-df1)**2.0)
    
    x3=x2-alpha*df2
    x0=x3
    f0=f(x0)
    print(j,'x',x0,'f',f0)