# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/5 21:00
# @file : 9.py
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        nums = [1] + nums
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1]
        l, r = 0, 0
        ans = float('inf')
        while r < len(nums):
            if nums[r] // nums[l] < k:
                r += 1
            else:
                ans = min(ans, r - l)
                l += 1
        return ans if ans != float('inf') else 0