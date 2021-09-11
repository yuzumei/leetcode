# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/10 23:19
# @file : 57.py
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        def getIdx(u):
            return ((u + 1) // size) - 1 if u < 0 else u // size

        map = {}
        size = t + 1
        for i, u in enumerate(nums):
            idx = getIdx(u)
            # 目标桶已存在（桶不为空），说明前面已有 [u - t, u + t] 范围的数字
            if idx in map:
                return True
            # 检查相邻的桶
            l, r = idx - 1, idx + 1
            if l in map and abs(u - map[l]) <= t:
                return True
            if r in map and abs(u - map[r]) <= t:
                return True
            # 建立目标桶
            map[idx] = u
            # 维护个数为k
            if i >= k:
                map.pop(getIdx(nums[i - k]))

        return False

x = Solution()
print(x.containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3))