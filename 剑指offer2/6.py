# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/5 0:55
# @file : 6.py
class Solution:
    def twoSum(self, numbers, target: int):
        l, r = 0, len(numbers)
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l, r]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1