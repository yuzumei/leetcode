# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/5 20:47
# @file : 8.py
class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        nums = [0] + nums
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        l, r = 0, 0
        ans = float('inf')
        while r < len(nums):
            if nums[r] - nums[l] < target:
                r += 1
            else:
                ans = min(ans, r - l)
                l += 1
        return ans if ans != float('inf') else 0


x = Solution()
print(x.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))