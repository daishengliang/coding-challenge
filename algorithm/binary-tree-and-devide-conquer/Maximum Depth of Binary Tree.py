"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example
Given a binary tree as follow:

  1
 / \ 
2   3
   / \
  4   5
The maximum depth is 3.


"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def maxDepth(self, root):
        # write your code here
        # Traverse
        self.depth = 0
        self.traverse(1, root)
        return self.depth
        
    def traverse(self, curr_depth, root):
        if root is None:
            return
        if curr_depth > self.depth:
            self.depth = curr_depth
            
        self.traverse(curr_depth + 1, root.left)
        self.traverse(curr_depth + 1, root.right)
