"""
Given a binary tree, return all root-to-leaf paths.

Example
Given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

[
  "1->2->5",
  "1->3"
]
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
    @param: root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        res = []
        if root == None:
            return res
            
        if root.left == None and root.right == None:
            res.append(str(root.val))
            return res

        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        for path in left:
            res.append(str(root.val) + '->' + path)
        for path in right:
            res.append(str(root.val) + '->' + path)
            
        return res