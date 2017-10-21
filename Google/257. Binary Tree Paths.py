"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        # DFS
        self.ans = []
        if not root:
            return self.ans

        
        def dfs(root, path):
            if root.left is None and root.right is None:
                self.ans.append(path)
            if root.left:
                dfs(root.left, path + '->' + str(root.left.val))
            if root.right:
                dfs(root.right, path + '->' + str(root.right.val))
                    
        dfs(root, str(root.val))
        return self.ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        # DFS
        self.ans = []
        if not root:
            return self.ans

        path = ""
        self.dfs(root, path)
        return self.ans
    
    def dfs(self, root, path):
        if root.left is None and root.right is None:
            path += str(root.val)
            self.ans.append(path)
        path += str(root.val)
        path += '->'    
        if root.left:  
            self.dfs(root.left, path)
        if root.right:
            self.dfs(root.right, path)   
