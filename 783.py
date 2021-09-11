class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.ans=float('inf')
        def find(node,flag):
            if not node:
                return float('inf')
            if flag==1:
                while node.left:
                    node=node.left
                return node.val
            else:
                while node.right:
                    node=node.right
                return node.right
        while root:
            self.ans=min(self.ans,root.val-find(root.left,0),find(root.right,1)-root.val)
            self.minDiffInBST(root.left)
            self.minDiffInBST(root.right)
        return self.ans
