"""
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

 Notice

Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.

Example
              1
               \
     1          2
    / \          \
   2   5    =>    3
  / \   \          \
 3   4   6          4
                     \
                      5
                       \
                        6
Challenge 
Do it in-place without any extra memory.

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
    @param: root: a TreeNode, the root of the binary tree
    @return: 
    """
    # Traversal
    
        
    def flatten(self, root):
        if root is None:
            return
        
        if self.last_node != None:
            self.last_node.right = root
            self.last_node.left = None
            
        self.last_node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)
    
    def __init__(self):
        self.last_node = None
    
"""        
# Devide and conquer
    def flatten(self, root):
        # write your code here
        self.helper(root)
        
    def helper(self, root):
        if root is None:
            return None
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left != None:
            left.right = root.right
            root.right = root.left
            root.left = None
        if right != None:
            return right
        if left != None:
            return left
        return root
"""
