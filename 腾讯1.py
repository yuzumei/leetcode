class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, h) -> TreeNode:
        import collections
        memo=collections.defaultdict(int)
        def depth(node):
            if not node:
                return 0
            memo[node]=1+max(depth(node.left),depth(node.right))
            return memo[node]
        depth(root)
        def search(node):
            ans=[]
            def find(node,l):
                if not node or l==-1:
                    return
                ans.append(node.val)
                find(node.left,l-1)
                find(node.right,l-1)
            find(node,h-1)
            return ans
        res=[]
        def preorder(node):
            if memo[node]<h:
                return
            res.append(search(node))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return res

x=TreeNode('a')
x.left=TreeNode('b')
x.right=TreeNode('c')
x.left.left=TreeNode('d')
x.left.right=TreeNode('e')
x.right.left=TreeNode('f')
x.right.right=TreeNode('g')
x.left.left.left=TreeNode('h')
x.left.right.right=TreeNode('i')
x.right.left.left=TreeNode('j')
x.right.right.right=TreeNode('k')
x.left.left.right=TreeNode('l')
x.left.right.left=TreeNode('m')
x.right.left.right=TreeNode('n')
x.right.right.left=TreeNode('o')
a=Solution()
print(a.lowestCommonAncestor(x,4))
