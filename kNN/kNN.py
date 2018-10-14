import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from Edge import Edge

plt.style.use('ggplot')
plt.ion()

def duplp(p1, p2):
    if p1[0] == p2[0] and p1[1] == p2[1]:
        return 1
    else:
        return 0

def validate(element):
    for i in range(len(S)):
        if S[i][0] == element[0] and S[i][1] == element[1]:
            return 1
    return 0

data = pd.read_csv('xclara.csv')

f1 = data['V1'].values
f2 = data['V2'].values

S = []
X = []
edges = []

X = np.array(list(zip(f1, f2)))
moda = len(X) % 2
min = Edge(np.array([0, 0]), np.array([50,50]), 1)

tempv = []
for j in range(len(X)):
    for k in range(len(X)):
        attempt = Edge(X[j], X[k], 0)
        if min.dist() > attempt.dist() and duplp(X[j], X[k]) == 0:
            min = attempt
            tempv = [j, k]

edges.append(min)
S.append(min.get()[0])
S.append(min.get()[1])
X = np.delete(X, tempv, axis=0)

pltEdgesX = []
pltEdgesY = []

for i in range(len(edges)):
    pltEdgesX.append(edges[i].get()[0][0])
    pltEdgesX.append(edges[i].get()[1][0])
    pltEdgesY.append(edges[i].get()[0][1])
    pltEdgesY.append(edges[i].get()[1][1])

plt.plot(pltEdgesX, pltEdgesY)
plt.scatter(f1, f2)

plt.draw()
plt.pause(2)
plt.clf()

seq = 1
size = len(X)

while size > moda:
    tempv = 0
    min = Edge(X[0], np.array((50,50)), seq)
    for n in range(len(S)):
        for j in range(len(X)):
            if validate(X[j]) != 1:
                attempt = Edge(S[n], X[j], seq)
                if min.dist() > attempt.dist():
                    min = attempt
                    tempv = j
    if validate(X[tempv]) != 1:
        edges.append(min)
        S.append(min.get()[1])
        seq = seq + 1
        size = size - 1

pltEdgesX = []
pltEdgesY = []

for i in range(len(edges)):
    pltEdgesX.append([edges[i].get()[0][0], edges[i].get()[1][0]])
    pltEdgesY.append([edges[i].get()[0][1], edges[i].get()[1][1]])

for i in range(len(pltEdgesX)):
    plt.plot(pltEdgesX[i], pltEdgesY[i])
plt.scatter(f1, f2)

plt.draw()
plt.pause(2)
plt.clf()

new_edge = []
for i in range(len(edges)):
    new_edge.append([edges[i].get(), edges[i].dist(), edges[i].getSeq()])
new_edge = np.array(new_edge)

k = 3

new_edge = new_edge[new_edge[:,1].argsort()]

size = len(new_edge) - 1
indexes = []
for i in range(0, k - 1):
    indexes.append(size)
    size -= 1
new_edge = np.delete(new_edge, indexes, axis=0)

pltEdgesX = []
pltEdgesY = []
for i in range(len(new_edge)):
    pltEdgesX.append([new_edge[i][0][0][0], new_edge[i][0][1][0]])
    pltEdgesY.append([new_edge[i][0][0][1], new_edge[i][0][1][1]])

for i in range(len(pltEdgesX)):
    plt.plot(pltEdgesX[i], pltEdgesY[i])
plt.scatter(f1, f2)

plt.ioff()
plt.show()