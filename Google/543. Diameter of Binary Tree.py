"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        根节点获取了左右子树的深度后，将二者相加就是该根节点下的Diameter。
        """
        if root is None:
            return 0

        l_height = self.height(root.left)
        r_height = self.height(root.right)
        height = l_height + r_height
        l_diameter = self.diameterOfBinaryTree(root.left)
        r_diameter = self.diameterOfBinaryTree(root.right)
        return max(height, l_diameter, r_diameter)
        

        
    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))