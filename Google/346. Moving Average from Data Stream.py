"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

"""
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = []
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.q) >= self.size:
            self.q.pop(0)
        self.q.append(val)
        return 1.0*sum(self.q)/len(self.q)


import collections
class MovingAverage2(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = collections.deque(maxlen=size)

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.append(val)
        return 1.0*sum(self.q)/len(self.q)
        