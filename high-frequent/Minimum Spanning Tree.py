"""
Given a list of Connections, which is the Connection class (the city name at both ends of the edge and a cost between them), find some edges, connect all the cities and spend the least amount.
Return the connects if can connect all the cities, otherwise return empty list.

 Notice

Return the connections sorted by the cost, or sorted city1 name if their cost is same, or sorted city2 if their city1 name is also same.


Example
Gievn the connections = ["Acity","Bcity",1], ["Acity","Ccity",2], ["Bcity","Ccity",3]

Return ["Acity","Bcity",1], ["Acity","Ccity",2]
"""
'''
Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''
class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        # Write your code here
        connections.sort(key = lambda x:[x.cost, x.city1, x.city2])
        
        dic = {}
        num = 0
        for i in connections:
            if i.city1 not in dic:
                num += 1
                dic[i.city1] = num
            if i.city2 not in dic:
                num += 1
                dic[i.city2] = num
                
        res = []
        father = [i for i in range(num + 1)]
        for i in connections:
            city1 = dic[i.city1]
            city2 = dic[i.city2]
            self.union(city1, city2, father, i, res)
            
        if len(res) == num - 1:
            return res
        return []
        
    def find(self, x, father):
        if father[x] == x:
            return x
        father[x] = self.find(father[x], father)
        return father[x]
        
    def union(self, a, b, father, connection, res):
        root_a = self.find(a, father)
        root_b = self.find(b, father)
        if root_a != root_b:
            father[root_a] = root_b
            res.append(connection)   