"""
Given a list of numbers, return all possible permutations.

 Notice

You can assume that there is no duplicate numbers in the list.

Example
For nums = [1,2,3], the permutations are:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
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
            line.append(elem)
            self.dfs(res, line, nums[:idx] + nums[idx + 1:])
            line.pop()            
