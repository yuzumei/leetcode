# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.counter = 0

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node:TreeNode, max_value:int) -> int:
            if not node: return
            else:
                # 如果存在比当前值大的计数器+1
                if node.val>=max_value:
                    self.counter += 1
                    max_value=node.val
                # 递归到叶子为止
                dfs(node.left, max_value)
                dfs(node.right, max_value)
        # 最小值切入
        dfs(root, float('-inf'))
        return self.counter
