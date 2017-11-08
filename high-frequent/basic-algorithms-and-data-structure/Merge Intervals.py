"""
Given a collection of intervals, merge all overlapping intervals.

Example
Given intervals => merged intervals:

[                     [
  [1, 3],               [1, 6],
  [2, 6],      =>       [8, 10],
  [8, 10],              [15, 18]
  [15, 18]            ]
]
Challenge 
O(n log n) time and O(1) extra space.
"""
class Solution:
    """
    @param: intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if not intervals:
            return []
        intervals.sort(key = lambda x : (x.start, x.end))
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(intervals[i].end, res[-1].end)
            else:
                res.append(intervals[i])
        return res