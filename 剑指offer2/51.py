# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/7 15:36
# @file : 51.py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = -float('inf')

    def maxPathSum(self, root: TreeNode) -> int:
        def func(root):
            if not root:
                return 0

            l = max(func(root.left), 0)
            r = max(func(root.right), 0)

            self.ans = max(self.ans, l + r + root.val)

            return max(l, r) + root.val
        func(root)
        return self.ans