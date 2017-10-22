"""
Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example:
nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

Result: [3, 9, 15, 33]

nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

Result: [-23, -5, 1, 7]
"""
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def f(x):
            return a*x**2 + b*x + c
        res = [0 for _ in range(len(nums))]
        
        if not nums:
            return res
            
        index = len(res) - 1 if a >= 0 else 0
        left = 0
        right = len(res) - 1
        while left <= right:
            if a >= 0:
                if f(nums[left]) >= f(nums[right]):
                    res[index] = f(nums[left])
                    left += 1
                else:
                    res[index] = f(nums[right])
                    right -= 1
                index -= 1
            else:
                if f(nums[left]) <= f(nums[right]):
                    res[index] = f(nums[left])
                    left += 1
                else:
                    res[index] = f(nums[right])
                    right -= 1
                index += 1
            
            
        return res