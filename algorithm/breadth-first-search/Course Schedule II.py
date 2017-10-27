"""
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example
Given n = 2, prerequisites = [[1,0]]
Return [0,1]

Given n = 4, prerequisites = [1,0],[2,0],[3,1],[3,2]]
Return [0,1,2,3] or [0,2,1,3]
"""
class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {int[]} the course order
    def findOrder(self, numCourses, prerequisites):
        # Write your code here
        indegree = {i : 0 for i in range(numCourses)}
        neighbors = {i : [] for i in range(numCourses)}
        
        for i, j in prerequisites:
            indegree[i] += 1
            neighbors[j].append(i)
        q = []
        res = []
        for key in indegree:
            if indegree[key] == 0:
                q.append(key)
                
        while q:
            node = q.pop(0)
            res.append(node)
            for nbs in neighbors[node]:
                indegree[nbs] -= 1
                if indegree[nbs] == 0:
                    q.append(nbs)
        if len(res) == numCourses:          
            return res
        else:
            return []