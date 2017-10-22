"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

 Notice

You may assume no duplicate exists in the array.

Example
Given [4, 5, 6, 7, 0, 1, 2] return 0
"""
class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        # write your code here
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        target = nums[end]
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            print(start, end, mid)
            if nums[mid] <= target:
                end = mid
            else:
                start = mid
                
        return min(nums[start], nums[end])
