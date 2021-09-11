# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode):
        ans=[]
        def searchpath(root):
            if root==None:
                ans.append(path)
                return []
            path=[]
            path+=root.val
            searchpath(root.left)
            searchpath(root.right)
