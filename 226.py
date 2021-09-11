# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def conver(root):
            if not root:
                return
            root.left,root.right=root.right,root.left
            conver(root.left)
            conver(root.right)
        conver(root)
        return root