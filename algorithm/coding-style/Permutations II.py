"""
Given a list of numbers with duplicate number in it. Find all unique permutations.

Example
For numbers [1,2,2] the unique permutations are:

[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]

"""
class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        res = []
        nums.sort()
        line = []
        self.dfs(res, line, nums)
        return res
        
    def dfs(self, res, line, nums):
        if len(nums) == 0:
            res.append([x for x in line])
        for idx, elem in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            line.append(elem)
            self.dfs(res, line, nums[:idx] + nums[idx + 1:])
            line.pop()  