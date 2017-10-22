"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3
Challenge 
Can you do it without recursion?
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
    @param: root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    # Iterative
    def inorderTraversal(self, root):
        stack = []
        res = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
                
    
"""
# Devide and Conquer
    def inorderTraversal(self, root):
        # write your code here
        res = []
        if root is None:
            return res
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        
        res += [x for x in left]
        res.append(root.val)
        res += [x for x in right]
        return res
"""        
        
"""
# Traversal
    def inorderTraversal(self, root):
        # write your code here
        res = []
        self.traverse(root, res)
        return res
        
    def traverse(self, root, res):
        if root is None:
            return
        self.traverse(root.left, res)
        res.append(root.val)
        self.traverse(root.right, res)
"""
