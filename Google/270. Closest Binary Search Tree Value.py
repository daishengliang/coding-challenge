"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

O(log n)
"""
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = root.val
        Max = 21474836470
        
        while root is not None:
            if abs(root.val - target) < Max:
                Max = abs(root.val - target)
                closest = root.val
            
            if target < root.val:
                root = root.left
            elif target > root.val:
                root = root.right
            else:
                return root.val
        return closest     
