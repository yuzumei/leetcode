# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/5 19:50
# @file : 5866.py
class UF:
    def __init__(self, n):
        self.parents = {i : i for i in range(n)}

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def merge(self, x, y):
        self.parents[self.find(x)] = self.parents[self.find(y)]

class Solution:
    def gcdSort(self, nums) -> bool:
        uf = UF(10 ** 5 + 1)
        def func(num):
            import math
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    uf.merge(num, i)
                    uf.merge(num, num // i)
        for num in nums:
            func(num)
        _pre, _next = dict(), dict()
        for i, num in enumerate(nums):
            temp = uf.find(num)
            if temp not in _pre:
                _pre[temp] = set()
            _pre[temp].add(i)
        nums.sort()
        for i, num in enumerate(nums):
            temp = uf.find(num)
            if temp not in _next:
                _next[temp] = set()
            _next[temp].add(i)
        print(_pre, _next)
        for item in _pre:
            if _pre[item] != _next[item]:
                return False
        return True

x = Solution()
print(x.gcdSort([10,5,9,3,20]))
