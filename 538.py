class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode):
        ans=[]
        def midfind(node):
            if node is None:
                return
            if node.left is None:
                ans.append(node)
            midfind(node.left)
            midfind(node.right)
        for i in range(len(ans)-2,-1,-1):
            ans[i].val+=ans[i+1].val
        return root

