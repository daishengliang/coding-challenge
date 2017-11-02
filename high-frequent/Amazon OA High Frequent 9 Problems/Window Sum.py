"""
Window Sum 

Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

Example
For array [1,2,7,8,5], moving window size k = 3. 
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
return [10,17,20]
"""
class Solution:
    # @param nums {int[]} a list of integers
    # @param k {int} size of window
    # @return {int[]} the sum of element inside the window at each moving
    def winSum(self, nums, k):
        # Write your code here
        if len(nums) < k or k <= 0:
            return []
            
        _sum = 0
        for i in range(k - 1):
            _sum += nums[i]
        ans = []
        j = 0
        for i in range(k - 1, len(nums)):
            _sum += nums[i]
            ans.append(_sum)
            _sum -= nums[j]
            j += 1
        return ans