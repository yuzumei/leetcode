# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/4 22:51
# @file : 4.py

class Solution:
    def singleNumber(self, nums) -> int:
        import math
        ans = [0] * 32
        self.flag = 0
        def func(num):
            if num == 0:
                return
            if num < 0:
                self.flag += 1
            num = num if num > 0 else -num
            cnt = int(math.log2(num)) + 1
            while num != 0:
                while num < 2 ** cnt:
                    cnt -= 1
                num -= 2 ** cnt
                ans[cnt] += 1
        for num in nums:
            func(num)
        res = 0
        for i, index in enumerate(ans):
            res += (index % 3) * 2 ** i
        return res if self.flag % 3 == 0 else -res

x = Solution()
print(x.singleNumber(nums = [-2,-2,1,1,4,1,4,4,-4,-2]))