"""
Given a list of numbers that may has duplicate numbers, return all possible subsets

 Notice

Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.

Example
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        res = []
        line = []
        S.sort()
        self.helper(S, res, line)
        return res
        
    def helper(self, S, res, line):
        res.append([x for x in line])
        for i, x in enumerate(S):
            if i > 0 and S[i-1] == S[i]:
                continue
            
            line.append(x)
            self.helper(S[i + 1:], res, line)
            line.pop()