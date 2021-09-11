class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        import collections
        res=collections.defaultdict(list)
        def find(root, i):
            if root == None:
                return
            res[i].append(root.val)
            find(root.left, i + 1)
            find(root.right, i + 1)
        find(root,0)
        ans=[]
        for item in res:
            ans.append(res[item])
        return ans