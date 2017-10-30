"""
Given some points and a point origin in two dimensional space, find k points out of the some points which are nearest to origin.
Return these points sorted by distance, if they are same with distance, sorted by x-axis, otherwise sorted by y-axis.

Example
Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
return [[1,1],[2,5],[4,4]]
"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Node:
    
    def __init__(self, dist, point):
        self.dist = dist
        self.point = point
        
    def __cmp__(self, other):
        if self.dist != other.dist:
            return other.dist - self.dist
        if self.point.x != other.point.x:
            return other.point.x - self.point.x
        return other.point.y - self.point.y

import heapq
class Solution:
    """
    @param: points: a list of points
    @param: origin: a point
    @param: k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        heap = []
        for i in points:
            dist = self.distance(i, origin)
            if len(heap) < k:
                heapq.heappush(heap, Node(dist, i))
            else:
                heapq.heappush(heap, Node(dist, i))
                heapq.heappop(heap)
        res = []
        while heap:
            res.insert(0, heapq.heappop(heap).point)
        return res
        
    def distance(self, a, b):
        return (a.x - b.x)**2 + (a.y - b.y)**2