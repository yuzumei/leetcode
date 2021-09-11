# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/11 0:09
# @file : 88.py
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        cost = [0] + cost + [0]
        ans = [float('inf')] * len(cost)
        ans[0] = 0
        for i in range(len(cost)):
            for j in range(1, 3):
                if i + j < len(cost):
                    ans[i + j] = min(ans[i + j], ans[i] + cost[i + j])
        return ans[-1]

x = Solution()
print(x.minCostClimbingStairs([10,15,20]))