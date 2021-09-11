# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/5 21:09
# @file : 11.py
class Solution:
    def findMaxLength(self, nums) -> int:
        import collections
        memo = collections.defaultdict(list)
        memo[0].append(-1)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
            if i >= 1:
                nums[i] += nums[i - 1]
            memo[nums[i]].append(i)
        ans = 0
        for item in memo:
            ans = max(memo[item][-1] - memo[item][0], ans)
        return ans

x =Solution()
print(x.findMaxLength([0,1,0]))