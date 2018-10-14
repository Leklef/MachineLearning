import numpy as np

class Edge:
  def __init__(self, start, end, seqence):
    self.start = start
    self.end = end
    self.seqence = seqence
  def get(self):
    return [self.start, self.end]
  def getSeq(self):
    return self.seqence
  def dist(self):
    return np.linalg.norm(self.get()[0]-self.get()[1])