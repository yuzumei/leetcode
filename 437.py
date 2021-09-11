class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.ans=0
        import collections
        memo=collections.defaultdict(int)
        memo[0]=1
        def dfs(node,cur):
            if not node:
                return
            cur+=node.val
            self.ans+=memo[cur-sum]
            memo[cur]+=1
            dfs(node.left,cur)
            dfs(node.right,cur)
            memo[cur] -= 1
        dfs(root,0)
        return self.ans
