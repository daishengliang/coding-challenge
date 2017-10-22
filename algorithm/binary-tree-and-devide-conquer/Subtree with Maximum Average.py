"""
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

 Notice

LintCode will print the subtree which root is your return node.

It's guaranteed that there is only one subtree with maximum average.

Example
Given a binary tree:

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
return the node 11.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def __init__(self):
        self.max_average = -1 << 31
        self.res = None

    def findSubtree2(self, root):
        # write your code here
        self.helper(root)
        return self.res
        
    def helper(self, root):
        if root == None:
            return [0, 0] #_sum, size
        left = self.helper(root.left)
        right = self.helper(root.right)
        num_nodes = left[1] + right[1] + 1
        _sum = left[0] + right[0] + root.val
        avg = _sum*1.0 / num_nodes
        if self.max_average < avg:
            self.max_average = avg
            self.res = root
        return _sum, num_nodes

