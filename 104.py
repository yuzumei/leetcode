class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans=1
        def find(root,i):
            global ans
            if root==None:
                ans=max(ans,i)
                return
            find(root.left,i+1)
            find(root.right,i+1)
        find(root,0)
        return ans