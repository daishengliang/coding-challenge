"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example
Given:

    1
   / \
  2   3
 / \
4   5
return [1,2,4,5,3].

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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        res = []
        self.traversal(root, res)
        return res

    def traversal(self, root, res):
        if root is not None:
            res.append(root.val)
            self.traversal(root.left, res)
            self.traversal(root.right, res)

"""
    # Devide and conquer
    def preorderTraversal(self, root):
        res = []
        if root is None:
            return res
        
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        res.append(root.val)
        res += [x for x in left]
        res += [x for x in right]
        return res
"""

""" 
    # Iterative 
    def preorderTraversal(self, root):
        # write your code here
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                res.append(curr.val)
                curr = curr.left
            curr = stack.pop()
            curr = curr.right
        return res
"""
