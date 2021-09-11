# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/4 18:15
# @file : 1.py

class Solution:
    def divide(self, a: int, b: int) -> int:
        if a < 0 and b < 0:
            return self.divide(-a, -b)
        if a < 0:
            return - self.divide(-a, b)
        if b < 0:
            return - self.divide(a, -b)
        ans = 0
        while a >= b:
            flag = 0
            while a >= b << flag:
                flag += 1
            ans += 1 << (flag - 1)
            a -= b << (flag - 1)
        return ans if ans <= (1 << 31) - 1 else (1 << 31) - 1

x = Solution()
print(x.divide(-2147483648,1))