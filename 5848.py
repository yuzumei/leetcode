# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/5 14:20
# @file : 5848.py
import collections
class LockingTree:

    def __init__(self, parent):
        '''[parent index, index]'''
        self.parent = [[parent[i], i] for i in range(len(parent))]
        self.parent.sort()
        self.parents = self.find_parent(self.parent)
        self.child = self.find_child(self.parent)
        '''memo each lock each user'''
        self.lock_memo = dict()

    def find_parent(self, parents):
        memo = dict()
        for i in range(len(parents)):
            if i == 0:
                memo[i] = []
            else:
                memo[parents[i][1]] = memo[parents[i][0]] + [parents[i][0]]
        return memo

    def find_child(self, parents):
        memo = dict()
        for i in range(len(parents) - 1, -1, -1):
            if parents[i][1] not in memo:
                memo[parents[i][1]] = []
            if parents[i][0] not in memo:
                memo[parents[i][0]] = []
            memo[parents[i][0]] += (memo[parents[i][1]] + [parents[i][1]])
        return memo

    def lock(self, num: int, user: int) -> bool:
        if num not in self.lock_memo:
            self.lock_memo[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.lock_memo:
            return False
        if self.lock_memo[num] == user:
            del self.lock_memo[num]
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        '''unlocked'''
        if num not in self.lock_memo:
            '''parent unlock'''
            for node in self.parents[num]:
                if node in self.lock_memo:
                    return False
            '''child lock at least 1'''
            flag = 0
            for node in self.child[num]:
                if node in self.lock_memo:
                    del self.lock_memo[node]
                    flag = 1
            if flag == 0:
                return False
            self.lock_memo[num] = user
            return True
        return False

x = LockingTree([-1,6,5,5,7,0,7,0,0,6])
print(x.parents,x.child)
