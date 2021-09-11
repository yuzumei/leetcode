# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d==1:
            node=TreeNode(v)
            node.left=root
            return node
        ans=[]
        def find(root,i,target):
            if root==None:
                return
            if i==target:
                ans.append(root)
                return
            find(root.left,i+1,target)
            find(root.right,i+1,target)
        find(root,1,d-1)
        for item in ans:
            nodeleft=TreeNode(v)
            noderight=TreeNode(v)
            nodeleft.left=item.left
            item.left=nodeleft
            noderight.right=item.right
            item.right=noderight
        return root



