"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

"""
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            dic = {}
            for j in range(len(points)):
                if i == j:
                    continue
                d = self.get_distance(points[i], points[j])
                if d not in dic:
                    dic[d] = 1
                else:
                    dic[d] += 1
            for key in dic:
                res += dic[key] * (dic[key] - 1)
            
        return res
    
    def get_distance(self, p1, p2):        
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2