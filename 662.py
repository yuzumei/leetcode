# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        import collections
        memo=collections.defaultdict(list)
        def search(node,i,p):
            if not node:
                return
            memo[i].append(p)
            search(node.left,i+1,2*p)
            search(node.right,i+1,2*p+1)
        search(root,0,0)
        ans=0
        for item in memo:
            temp=memo[item]
            ans=max(ans,temp[-1]-temp[0]+1)
        return ans
