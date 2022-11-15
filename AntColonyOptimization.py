# -*- coding: utf-8 -*-
"""
Created on Fri May 21 17:41:51 2021

@author: Basheer
"""

"Ant Colony Optimization"

import numpy as np

nants=10
rho=0.8
alpha=1         #Pheromone
beta=1          #Visibility
iterations=20
cities=5
coords=np.zeros([cities,2])
dist=np.zeros([cities,cities])
pheromone=np.ones([cities,cities])
probabilities=np.ones([cities,cities])
vis=np.zeros([cities,cities])
coords[0,:]=10,2
coords[1,:]=100,5
coords[2,:]=70,80
coords[3,:]=4,-30
coords[4,:]=16,1
for c in range(cities):
    for d in range(cities):
        dist[c,d]=np.sqrt((coords[c,0]-coords[d,0])**2+(coords[c,1]-coords[d,1])**2)
        if (c==d):
            vis[c,d]=0.0
            pheromone[c,d]=0.0
            probabilities[c,d]=0.0
        else:
            vis[c,d]=1/dist[c,d]
    
tour=cities*np.ones([nants,cities+1])
tour[:,0]=0
tour[:,cities]=0
dists=np.zeros(cities)
tourcity=cities*np.ones([nants,cities,2])

for itr in range(iterations):
    
    print('Iteration:',itr)
    for ant in range(nants):
        for trip in range(1,cities):
            #print(probabilities)
            #print(max(probabilities[int(tour[ant,trip-1])]))
            for pr in range(cities):
                probabilities[pr,pr]=0
            #print(probabilities)
            b=probabilities[int(tour[ant,trip-1]),:].argmax()
            probabilities[int(tour[ant,trip-1]),:]=0
            probabilities[:,int(tour[ant,trip-1])]=0
            #print(probabilities)
            tour[ant,trip]=b
            tour=tour.astype(int)
            tourcity[ant,trip,:]=coords[tour[ant,trip],:]
            
        for tr in range(cities):
            sx=(coords[tour[ant,tr+1],0]-coords[tour[ant,tr],0])**2
            sy=(coords[tour[ant,tr+1],1]-coords[tour[ant,tr],1])**2
            dists[tr]=np.sqrt(sx+sy)
        dpher=1/sum(dists)
        pheromone=(1-rho)*pheromone+dpher
        pin=pheromone**alpha
        vin=vis**beta
        prod=pin*vin
        probabilities=prod/sum(sum(prod))
print(tour)