# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int):
        ans=[]
        def searchpath(root,path):
            if root is None:
                return
            if root==target:
                temp=path+[root]
                ans.append(temp)
                return
            temp=path+[root]
            searchpath(root.left,temp)
            searchpath(root.right,temp)

        res=[]
        def find(root,i,tar):
            if root==None:
                return
            if i==tar:
                res.append(root.val)
                return
            find(root.left,i+1,tar)
            find(root.right,i+1,tar)
        n=len(ans)
        find(root,0,K)
        if n>K:
            res.append(ans[n-1-K].val)
            for i in range(n-K,n-1):
                if ans[i].left==ans[i+1]:
                    find(root.right,0,K-n+i)
                else:
                    find(root.left, 0, K - n + i)
        else:
            for i in range(0,n-1):
                if ans[i].left==ans[i+1]:
                    find(root.right,0,K-n+i)
                else:
                    find(root.left, 0, K - n + i)
        print(res)

