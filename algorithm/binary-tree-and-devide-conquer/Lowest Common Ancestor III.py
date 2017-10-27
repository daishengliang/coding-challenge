"""
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
Return null if LCA does not exist.

 Notice

node A or node B may not exist in tree.

Example
For the following binary tree:

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
import copy
class ResultType:
    
    def __init__(self, a, b, n):
        self.a_exist = a
        self.b_exist = b
        self.node = n

class Solution:
    """
    @param {TreeNode} root The root of the binary tree.
    @param {TreeNode} A and {TreeNode} B two nodes
    @return Return the LCA of the two nodes.
    """ 
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        res = self.helper(root, A, B)
        if res.a_exist and res.b_exist:
            return res.node
        return None
        
    def helper(self, root, A, B):
        if root is None:
            return ResultType(False, False, root)
        if root is A:
            a_exist = True
        else:
            a_exist = False

        if root is B:
            b_exist = True
        else:
            b_exist = False
        left = self.helper(root.left, A, B)
        right = self.helper(root.right, A, B)
        a_exist |= left.a_exist or right.a_exist
        b_exist |= left.b_exist or right.b_exist
        
        if root is A or root is B:
            return ResultType(a_exist, b_exist, root)
        if left.node is not None and right.node is not None:
            return ResultType(a_exist, b_exist, root)
        if left.node is not None:
            return ResultType(a_exist, b_exist, left.node)
        if right.node is not None:
            return ResultType(a_exist, b_exist, right.node)
        return ResultType(a_exist, b_exist, None)
