# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/4 16:13
'''
@file: 673.py
@time: 2021/09/{DAY}
'''
class Solution:
    def findNumberOfLIS(self, nums) -> int:
        N = len(nums)
        if N <= 1: return N
        lengths = [0] * N  # lengths[i] = longest ending in nums[i]
        counts = [1] * N  # count[i] = number of longest ending in nums[i]

        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)


