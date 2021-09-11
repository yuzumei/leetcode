# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/5 0:43
# @file : 5.py
class Solution:
    def maxProduct(self, words) -> int:
        def transform(word):
            res = [0] * 26
            for s in word:
                res[ord(s) - ord('a')] = 1
            ans = sum(res[i] * 2 ** i for i in range(26))
            return ans
        ans = 0
        nums = [[transform(word), len(word)] for word in words]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i][0] & nums[j][0] == 0:
                    ans = max(ans, nums[i][1] * nums[j][1])
        return ans

x = Solution()
print(x.maxProduct(words = ["abcw","baz","foo","bar","fxyz","abcdef"]))