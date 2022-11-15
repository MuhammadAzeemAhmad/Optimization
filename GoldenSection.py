# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 08:45:48 2021

@author: Basheer
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 09:39:55 2021

@author: Basheer
"""

import numpy as np
import matplotlib.pyplot as plt
from array import *

def f(x):
    return 1/4*x**4-5/3*x**3-6*x**2+19*x-7

msg="Golden Section Search"
print(msg)

xl=-4.0
xu=0.0
dx=0.01
n=20
Tol=0.00001
i=0
phi=(1.0+5.0**(1/2))/2
I=array('d',[xu-xl])    
for j in range(n-1):
    i=n-j-2
    #print(i)
    #print(i-1)
    I.append(I[j]/phi)
    
xa=xu-I[1]
xb=xl+I[1]
fa=f(xa)
fb=f(xb)
#print(F)
#print(I)

for j in range(n-2):
#while (abs(fb-fa)>Tol):
    x=np.linspace(xl,xu,100)
    y=f(x)
    plt.plot(x,y)
    plt.show()
    print('Iteration: ',j)
    print('XL:',xl,'XU:',xu,'XA',xa,'fxa:',fa,'XB',xb,'fxb',fb)
    fa=f(xa)
    fb=f(xb)

    if (fb<fa):
        xl=xa
        xa=xb
        xb=xl+I[j+2]
    else:
        xu=xb
        xb=xa
        xa=xu-I[j+2]
    