# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''前序：HGEDBFCA
            中序：EGBDHFAC'''
        memo1={num:i for i,num in enumerate(inorder)}
        n=len(preorder)
        def build(start,end,memo):
            if start>end:
                return
            node=preorder[start]
            splitpoint=memo1[node]
            root=TreeNode(node)
            length=splitpoint-memo
            root.left=build(start+1,start+length,memo)
            root.right=build(start+length+1,end,splitpoint+1)
            return root
        return build(0,n-1,0)
        # n=len(preorder)
        # def build(start,end,memo):
        #     if start>end:
        #         return None
        #     node=preorder[start]
        #     nodeindex=memo1[node]
        #     length=nodeindex-memo
        #     root=TreeNode(node)
        #     root.left=build(start+1,start+length,memo)
        #     root.right=build(start+length+1,end,nodeindex+1)
        #     return root
        # return build(0,n-1,0)

class Solution1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root=TreeNode(preorder[0])
        stack=[root]
        inorderindex=0
        for i in range(1,len(preorder)):
            leftend=inorder[inorderindex]
            preval=preorder[i]
            node=stack[-1]
            if node.val!=leftend:
                node.left=TreeNode(preval)
                stack.append(node.left)
            else:
                while stack and stack[-1].val==inorder[inorderindex]:
                    node=stack.pop()
                    inorderindex+=1
                node.right=TreeNode(preval)
                stack.append(node.right)
        return root
