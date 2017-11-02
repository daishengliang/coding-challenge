"""
Given a binary tree, find the subtree with maximum sum. Return the root of the subtree.

 Notice

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum sum and the given binary tree is not an empty tree.


Example
Given a binary tree:

     1
   /   \
 -5     2
 / \   /  \
0   3 -4  -5 
return the node with value 3.
"""
class Solution:
    """
    @param: root: the root of binary tree
    @return: the maximum weight node
    """
    def __init__(self):
        self.int_min = -1 << 31
        self.res = None
        
    def findSubtree(self, root):
        if not root:
            return None
            
        self.helper(root)
        return self.res
        
    def helper(self, root):
        # write your code here
        if not root:
            return 0
            
        left = self.helper(root.left)
        right = self.helper(root.right)
        ans = left + right + root.val
        if ans > self.int_min:
            self.int_min = ans
            self.res = root
        return ans
            
        