class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        import collections
        f=collections.defaultdict(int)   #包含此节点
        g=collections.defaultdict(int)   #不包含此节点
        memo=collections.defaultdict(list)
        def travel(node,i):
            if node==None:
                return
            memo[i].append(node)
            travel(node.left,i+1)
            travel(node.right,i+1)
        travel(root,1)
        n=max(memo)
        for i in range(n,0,-1):
            for item in memo[i]:
                if item.left and item.right:
                    f[item]=item.val+g[item.left]+g[item.right]
                    g[item]=max(f[item.left],g[item.left])+max(f[item.right],g[item.right])
                elif item.left:
                    f[item]=item.val+g[item.left]
                    g[item]=max(f[item.left],g[item.left])
                elif item.right:
                    f[item]=item.val+g[item.right]
                    g[item]=max(f[item.right],g[item.right])
                else:
                    f[item]=item.val
                    g[item]=0
        return max(f[root],g[root])

