class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        import collections
        memo=collections.defaultdict(list)
        def pre(node,i):
            if not node:
                return
            memo[i].append(node)
            pre(node.left,i+1)
            pre(node.right,i+1)
        pre(root,0)
        ans=[]
        for i in memo:
            if i%2==0:
                ans.append(memo[i])
            else:
                ans.append((memo[i][::-1]))
        return ans