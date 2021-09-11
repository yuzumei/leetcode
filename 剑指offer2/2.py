# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/4 18:52
# @file : 2.py
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            return self.addBinary(b, a)
        b = (len(a) - len(b)) * '0' + b
        ans = ''
        owe = 0
        n = len(a)
        for i in range(n):
            index = n - 1 - i
            total = int(a[index]) + int(b[index]) + owe
            t_owe = 1 if total >= 2 else 0
            t = (total - 2 * t_owe) % 2
            owe = t_owe
            ans = str(t) + ans
        if owe == 0:
            return ans
        else:
            return str(owe) + ans

x = Solution()
print(x.addBinary(a = "11000", b = "10"))