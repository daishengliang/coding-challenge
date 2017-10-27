"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example
An example:

  2
 / \
1   4
   / \
  3   5
The above binary tree is serialized as {2,1,4,#,#,3,5} (in level order).
"""


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

# Inorder traversal
    def isValidBST(self, root):
        stack = []
        prev = -sys.maxint - 1

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True
            

"""
    def isValidBST(self, root):
        # write your code here
        lower_bound = -1 << 61
        upper_bound = 1 << 61 
        return self.helper(root, lower_bound, upper_bound)
        
        
    def helper(self, root, lower_bound, upper_bound):
        if root is None:
            return True
        
        if root.val >= upper_bound or root.val <= lower_bound:
            return False
        
        return self.helper(root.left, lower_bound, root.val) and self.helper(root.right, root.val, upper_bound)
"""