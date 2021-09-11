# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/7 14:58
# @file : 63.py
class Trie:
    def __init__(self, words):
        self.wordtree = dict()
        for word in words:
            temp = self.wordtree
            for s in word:
                if s not in temp:
                    temp[s] = dict()
                temp = temp[s]
            temp['leaf'] = word

class Solution:
    def replaceWords(self, dictionary, sentence: str) -> str:
        trie = Trie(dictionary)
        words = sentence.split()
        ans = ''
        for word in words:
            temp = ''
            cur_trie = trie.wordtree
            for s in word:
                if 'leaf' in cur_trie:
                    temp = cur_trie['leaf']
                    break
                if s not in cur_trie:
                    temp = word
                    break
                temp += s
                cur_trie = cur_trie[s]
            ans += (word + ' ')
        return ans[:-1]