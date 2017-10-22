"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        if not A or target is None:
            return -1
        start = 0
        end = len(A) - 1
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] > A[-1]:
                if A[start] <= target and target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if target <= A[end] and target >= A[mid]:
                    start = mid
                else:
                    end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
