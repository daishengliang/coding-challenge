"""
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

Given graph:

[
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]
return 3
"""
class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        if not grid:
            return 0
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        if not n:
            return 0
            
        union_find = Union_find(m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    id = self.convert_to_id(i, j, n)
                    if union_find.father[id] == -1:
                        union_find.father[id] = id
                    union_find.total += 1
                    
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    id = self.convert_to_id(i, j, n)
                    for idx in range(len(dx)):
                        nx = i + dx[idx]
                        ny = j + dy[idx]
                        if self.isvalid(nx, ny, m, n):
                            nid = self.convert_to_id(nx, ny, n)
                            union_find.union(nid, id)
        return union_find.query()
        
    def isvalid(self, nx, ny, m, n):
        return nx >= 0 and nx < m and ny >= 0 and ny < n
            
    def convert_to_id(self, x, y, n):
        return x * n + y
        
class Union_find(object):
    # O(4k + m*n) m*n is for init
    def __init__(self, n):
        self.father = [-1 for _ in range(n)]
        self.total = 0
            
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
            
    def union(self, a, b):
        if self.father[a] == -1 or self.father[b] == -1:
            return False
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.total -= 1
                
    def query(self):
        return self.total
            
