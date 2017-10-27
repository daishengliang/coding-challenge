"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7
 

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
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
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        res = []
        if root is None:
            return res
        level = []
        q = [root]
        while q:
            size = len(q)
            for _ in range(size):
                head = q.pop(0)
                level.append(head.val)
                if head.left:
                    q.append(head.left)
                if head.right:
                    q.append(head.right)
            res.append([x for x in level])
            level = []
        return res