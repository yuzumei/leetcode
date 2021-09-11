# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans=[]
        def firstsearch(node):
            if node==None:
                return
            ans.append(node)
            firstsearch(node.left)
            firstsearch(node.right)
        firstsearch(root)
        for i in range(len(ans)-1):
            ans[i].left=None
            ans[i].right=ans[i+1]