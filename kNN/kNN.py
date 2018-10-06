import random
import math
import pylab as plt
import numpy as np
from matplotlib.colors import ListedColormap

def generateData (numberOfClassEl, numberOfClasses):
    data = []
    for classNum in range(numberOfClasses):
        centerX, centerY = random.random()*5.0, random.random()*5.0
        for rowNum in range(numberOfClassEl):
            data.append([ [random.gauss(centerX,0.5), random.gauss(centerY,0.5)], classNum])
    return data

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def knn(train, test, k, numberOfClasses):
    for point in test:
        labels = []
        dist = [[distance(point, train[i][0]), train[i][1]] for i in range(len(train))]
        stat = [0 for i in range(numberOfClasses)]
        for d in sorted(dist)[0:k]:
            stat[d[1]] += 1
        labels.append(sorted(zip(stat, range(numberOfClasses)), reverse=True)[0][1])
    return labels