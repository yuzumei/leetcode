# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/4 22:16
# @file : 3.py
class Solution:
    def countBits(self, n: int):
        import math
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            index = int(math.log2(i))
            ans[i] = 1 + ans[i - 2 ** index]
        return ans

x = Solution()
print(x.countBits(5))