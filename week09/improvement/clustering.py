"""This code implements the k-means clustering algorithm for 2 dimensions."""

from math import *
from random import *

k_means_clusters=3
number_of_ttl_iterations = 10

lines = open('samples.csv', 'r').readlines()
points=[]

for line in lines: points.append(tuple(map(float, line.strip().split(','))))

means =[]
for m in range(k_means_clusters): means.append(points[randrange(len(points))])

alloc=[None]*len(points)

n=0
while n < number_of_ttl_iterations:
  for i,p in enumerate(points):
    d=[None] * k_means_clusters
    d[0]=sqrt((p[0]-means[0][0])**2 + (p[1]-means[0][1])**2)
    d[1]=sqrt((p[0]-means[1][0])**2 + (p[1]-means[1][1])**2)
    d[2]=sqrt((p[0]-means[2][0])**2 + (p[1]-means[2][1])**2)
    alloc[i]=d.index(min(d))
  for i in range(k_means_clusters):
    alloc_ps=[p for j, p in enumerate(points) if alloc[j] == i]
    new_mean=(sum([a[0] for a in alloc_ps]) / len(alloc_ps), sum([a[1] for a in alloc_ps]) / len(alloc_ps))
    m[i]=new_mean
  n=n+1

for i in range(k_means_clusters):
  alloc_ps=[p for j, p in enumerate(ps) if alloc[j] == i]
  print("Cluster " + str(i) + " is centred at " + str(m[i]) + " and has " + str(len(alloc_ps)) + " points.")