class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        '''后序序列为: EBDGACFH
        中序：EGBDHFAC'''
        # memo1={item:i for i,item in enumerate(inorder)}
        n=len(inorder)
        # def build(start,end,memo):
        #     if start<end:
        #         return
        #     node=postorder[start]
        #     root=TreeNode(node)
        #     target=memo1[node]
        #     length=memo-target
        #     root.left=build(start-length-1,end,target)
        #     root.right=build(start-1,start-length,memo)
        #     return root
        # return build(n-1,0,n-1)
        #
        if not inorder:
            return None
        root=TreeNode(postorder[-1])
        stack=[root]
        inordindex=n-1
        for i in range(n-2,-1,-1):
            node=stack[-1]
            temp=inorder[inordindex]
            target=postorder[i]
            if node.val!=temp:
                node.right=TreeNode(target)
                stack.append(node.right)
            else:
                while stack and stack[-1]==inorder[inordindex]:
                    node=stack.pop()
                    inordindex-=1
                node.left=TreeNode(target)
                stack.append(node.left)
        return root
