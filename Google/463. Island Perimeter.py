"""
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:

"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                if i == 0 or grid[i - 1][j] == 0:
                    res += 1
                if j == 0 or grid[i][j - 1] == 0:
                    res += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    res += 1
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    res += 1
        return res
        