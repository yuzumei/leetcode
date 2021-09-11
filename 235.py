class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        memo=dict()
        def match(node,i,num):
            if not node:
                return
            if p.val in memo and q.val in memo:
                return
            memo[node]=[i,num]
            match(node.left,i+1,num*2-1)
            match(node.right,i+1,num*2)
        match(root,0,1)
        pindex=memo[p][:]
        qindex=memo[q][:]
        while pindex!=qindex:
            if pindex[0]>qindex[0]:
                pindex[0]-=1
                pindex[1]=int((pindex[1]+1)/2)
            elif pindex[0]<qindex[0]:
                qindex[0]-=1
                qindex[1]=int((qindex[1]+1)/2)
            else:
                pindex[0]-=1
                pindex[1]=int((pindex[1]+1)/2)
                qindex[0]-=1
                qindex[1]=int((qindex[1]+1)/2)
        for num in memo:
            if memo[num]==pindex:
                return num
