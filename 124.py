root = [-10,9,20,null,null,15,7]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans=-float('inf')
        import collections
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
            temp=memo[i]
            for item in temp:
                if item.right and item.left:
                    ans = max(ans, item.val, item.val + item.left.val, item.val + item.right.val,
                              item.val + item.left.val + item.right.val)
                    item.val=max(item.val,item.val+item.left.val,item.val+item.right.val)
                elif item.right:
                    ans=max(ans,item.val,item.val+item.right.val)
                    item.val=max(item.val,item.val+item.right.val)
                elif item.left:
                    ans=max(ans,item.val,item.val+item.left.val)
                    item.val=max(item.val,item.val+item.left.val)
                else:
                    ans=max(ans,item.val)
        return ans