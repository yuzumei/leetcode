class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        if not root.left and not root.right:
            return True
        def search(root,small,big):
            if not root:
                return
            if root.val<small or root.val>big:
                return False
            if root.left:
                search(root.left,small,root.val)
            if root.right:
                search(root.right,root.val,big)
            return True
        return search(root,-float('inf'),float('inf'))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            return True
        def search(root,small,big):
            if not root:
                return True
            if root.val<=small or root.val>=big:
                return
            if not search(root.left,small,root.val):
                return False
            if not search(root.right,root.val,big):
                return False
            return True
        return search(root,-float('inf'),float('inf'))
