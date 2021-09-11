# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/10 18:15
# @file : 84.py
class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        ans = []
        res = []
        n = len(nums)
        visited = [0] * len(nums)
        def dfs():
            if len(res) == n:
                ans.append(res[:])
            for i in range(n):
                if visited[i] == 1 or (i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 1):
                    continue
                res.append(nums[i])
                visited[i] = 1
                dfs()
                res.pop()
                visited[i] = 0
        dfs()
        return ans

x = Solution()
print(x.permuteUnique([1,1,1,1,2]))