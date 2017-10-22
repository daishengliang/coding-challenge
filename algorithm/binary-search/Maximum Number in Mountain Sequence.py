"""
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.

Example
Given nums = [1, 2, 4, 8, 6, 3] return 8
Given nums = [10, 9, 8, 7], return 10
"""
class Solution:
    # @param {int[]} nums a mountain sequence which increase firstly and then decrease
    # @return {int} then mountain top
    def mountainSequence(self, nums):
        # Write your code here
        if not nums or len(nums) == 0:
            return 0
            
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
        return max(nums[start], nums[end])