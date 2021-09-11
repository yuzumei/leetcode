# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/5 15:04
# @file : 5849.py
class Solution:
    def numberOfGoodSubsets(self, nums) -> int:
        pre = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        need = pre + [6, 10, 14, 15, 21, 22, 26, 30]
        need = set(need)
        cnt = 1
        new_nums = dict()
        for num in nums:
            if num in need:
                if num not in new_nums:
                    new_nums[num] = 0
                new_nums[num] += 1
            if num == 1:
                cnt += 1
        keys = list(new_nums.keys())
        keys.sort()
        '''合数和质数部分设为0'''
        n = len(keys)
        dy = [1] * (1 << n)

        temp = {keys[i] : i for i in range(len(keys))}
        for i, item in enumerate(keys):
            if item != 2 and item != 3 and item != 5:
                if item % 2 == 0:
                    res = item // 2
                    if 2 in temp:
                        dy[(1 << i) + (1 << temp[2])] = 0
                    if res in temp:
                        dy[(1 << i) + (1 << temp[res])] = 0
                if item % 3 == 0:
                    res = item // 3
                    if 3 in temp:
                        dy[(1 << i) + (1 << temp[3])] = 0
                    if res in temp:
                        dy[(1 << i) + (1 << temp[res])] = 0
                if item % 5 == 0:
                    res = item // 5
                    if 5 in temp:
                        dy[(1 << i) + (1 << temp[5])] = 0
                    if res in temp:
                        dy[(1 << i) + (1 << temp[res])] = 0

        for i in range(1 << n):
            if dy[i] != 0:
                j = 0
                while i > (1 << j):
                    if i & (1 << j) != 0 and dy[i - (1 << j)] == 0:
                        dy[i] = 0
                        break
                    j += 1

        numss = [1] * (1 << n)
        for num in new_nums:
            numss[1 << temp[num]] = new_nums[num]

        for i in range(1, 1 << n):
            temp = 1
            for j in range(n):
                temp *= numss[i & (1 << j)]
            numss[i] = temp

        print(keys)
        print(dy)
        print(numss)
        ans = 0
        for i in range(1, 1 << n):
            ans += numss[i] * dy[i]
            ans %= (10 ** 9 + 7)

        return (ans * cnt) % (10 ** 9 + 7)

x = Solution()
print(x.numberOfGoodSubsets([30,28,26,30,19,12,12,25,12]))
