class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans={p:[],q:[]}
        def dfs(node,target):
            if not node:
                return False
            if node==target:
                ans[target].append(node)
                return True
            if dfs(node.left,target):
                ans[target].append(node)
            if dfs(node.right,target):
                ans[target].append(node)
        dfs(root,p)
        dfs(root,q)
        for item in ans[p][::-1]:
            if item in ans[q]:
                return item