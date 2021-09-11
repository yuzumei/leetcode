# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/10 23:58
# @file : 62.py
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.parents = dict()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self.parents
        for s in word:
            if s not in temp:
                temp[s] = dict()
            temp = temp[s]
        temp['leaf'] = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self.parents
        for s in word:
            if s not in temp:
                return False
            temp = temp[s]
        if 'leaf' in temp:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.parents
        for s in prefix:
            if s not in temp:
                return False
            temp = temp[s]
        return True