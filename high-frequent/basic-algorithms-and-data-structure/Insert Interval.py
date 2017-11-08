"""
Given a non-overlapping interval list which is sorted by start point.

Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).

Example
Insert [2, 5] into [[1,2], [5,9]], we get [[1,9]].

Insert [3, 4] into [[1,2], [5,9]], we get [[1,2], [3,4], [5,9]].
"""


#Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end



class Solution:
    """
    @param: intervals: Sorted interval list.
    @param: newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        index = 0
        while index < len(intervals):
            if intervals[index].start >= newInterval.start:
                break
            index += 1
        intervals.insert(index, newInterval)
        prev = None
        res = []
        for i in intervals:
            if prev == None or prev.end < i.start:
                res.append(i)
                prev = i
            else:
                prev.end = max(prev.end, i.end)
        return res
s = Solution()
intervals = [Interval(1, 2), Interval(5, 9)]
newInterval = Interval(2, 5)
res = s.insert(intervals, newInterval)
for i in res:
 	print(i.start, i.end)
