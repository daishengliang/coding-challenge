"""
Given a set of distinct integers, return all possible subsets.

 Notice

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

Example
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""
class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        S.sort()
        self.res = []
        line = []
        self.dfs(line, S)
        return self.res
        
    def dfs(self, line, S):
        self.res.append([x for x in line])
        
        for i in range(len(S)):
            line.append(S[i])
            self.dfs(line, S[i + 1:])
            line.pop()