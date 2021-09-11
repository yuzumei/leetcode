# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/5 16:49
# @file : 5864.py
class Solution:
    def numberOfWeakCharacters(self, properties) -> int:
        properties.sort(key = lambda x:(-x[0], x[1]))
        value = 0
        ans = 0
        for item in properties:
            if item[1] < value:
                ans += 1
            else:
                value = item[1]
        return ans
        # def merge(x, y):
        #     res = []
        #     while x and y:
        #         if x[0][1] > y[-1][1]:
        #             res.append(x.pop(0))
        #         else:
        #             res.append(y.pop())
        #     if x:
        #         return res + x
        #     if y:
        #         return res + y[::-1]
        #     return res
        # properties.sort(key = lambda x:(x[0], x[1]))
        # past, cur = [], []
        # ans = 0
        # cur_num = properties[0][0]
        # for item in properties:
        #     if item[0] == cur_num:
        #         cur.append(item)
        #     else:
        #         '''进入新的值 past和cur合并 cur清空 past为单调栈'''
        #         past = merge(past, cur)
        #         cur, cur_num = [item], item[0]
        #     while past and past[-1][1] < item[1]:
        #         past.pop()
        #         ans += 1
        # return ans

x = Solution()
print(x.numberOfWeakCharacters([[1,5],[10,4],[4,3]]))