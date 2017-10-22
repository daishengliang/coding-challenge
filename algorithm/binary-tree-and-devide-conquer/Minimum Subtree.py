"""
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

 Notice

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

Example
Given a binary tree:

     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5 
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
    @return: the root of the minimum subtree
    """
    def __init__(self):
        self.max_val = 1 << 31 - 1
        self.res = None
        
    def findSubtree(self, root):
        self.findSubtree_helper(root)
        return self.res

    def findSubtree_helper(self, root):
        # write your code here
        if root == None:
            return 0
        left = self.findSubtree_helper(root.left)
        right = self.findSubtree_helper(root.right)
        _sum = left + right + root.val
        if _sum < self.max_val:
            self.max_val = _sum
            self.res = root
        return _sum
