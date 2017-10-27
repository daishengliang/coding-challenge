"""
Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

A valid path is from root node to any of the leaf nodes.

Example
Given a binary tree, and target = 5:

     1
    / \
   2   4
  / \
 2   3
return

[
  [1, 2, 2],
  [1, 4]
]
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        res = []
        if root is None:
            return res
        if root.left is None and root.right is None and target == root.val:
            res.append([root.val])
            
        left = self.binaryTreePathSum(root.left, target - root.val)
        right = self.binaryTreePathSum(root.right, target - root.val)
        
        for path in left:
            res.append([root.val] + path)
        for path in right:
            res.append([root.val] + path)
        return res

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        res = []
        line = []
        self.helper(root, target, res, line)
        return res
        
    def helper(self, root, target, res, line):
        if root is None:
            return
        line.append(root.val)
        if root.left is None and root.right is None and root.val == target:
            res.append([x for x in line])
            line.pop()
            return
            
        self.helper(root.left, target - root.val, res, line)
        self.helper(root.right, target - root.val, res, line)
        line.pop()
        return