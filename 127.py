beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log",'cog']
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        import collections
        memo=collections.defaultdict(set)
        trans=collections.defaultdict(list)
        n=len(beginWord)
        for word in wordList:
            for i in range(n):
                temp=word[:i]+'*'+word[i+1:]
                for item in trans[temp]:
                    memo[item].add(word)
                    memo[word].add(item)
                trans[temp].append(word)
        for i in range(n):
            temp=beginWord[:i]+'*'+beginWord[i+1:]
            for item in trans[temp]:
                memo[beginWord].add(item)
        queue=[beginWord]
        cnt={item:float('inf') for item in wordList}
        cnt[beginWord]=1
        cnt[endWord]=float('inf')
        while queue:
            temp=queue.pop(0)
            for item in memo[temp]:
                if cnt[item]>cnt[temp]:
                    cnt[item]=cnt[temp]+1
                    queue.append(item)
        return 0 if cnt[endWord]==float('inf') else cnt[endWord]
x=Solution()
print(x.ladderLength(beginWord,endWord,wordList))
# class Trie:
#     def __init__(self,words):
#         self.root={}
#         for word in words:
#             temp=self.root
#             for c in word:
#                 if c not in temp:
#                     temp[c]={}
#                 temp=temp[c]
#             temp["leaf"]=word
#
#     def allword(self,words):
#         from collections import defaultdict
#         ans=defaultdict(set)
#         for word in words:
#             for i in range(len(word)):
#                 ans[i].add(word[i])
#         return ans
#
#     def search(self,word):
#         start=self.root
#         for c in word:
#             if c not in start:
#                 return False
#             start=start[c]
#         if "leaf" in start:
#             return True
# import time
# def ladderLength(beginWord, endWord, wordList):
#     time1=time.time()
#     from collections import defaultdict
#     trie = Trie(wordList + [beginWord])
#     if not trie.search(endWord):
#         return 0
#     memo=defaultdict(int)
#     time2=time.time()
#     for word in wordList:
#         memo[word]=10000
#     memo[beginWord]=1
#     memo[endWord]=10000
#     alpha=trie.allword(wordList)
#     print(alpha)
#     words=[beginWord]
#     while memo[endWord]==10000:
#         temp=[]
#         for item in words:
#             for i in range(len(item)):
#                 for x in alpha[i]:
#                     newword=item[:i]+x+item[i+1:]
#                     if trie.search(newword) and memo[newword]==10000:
#                         memo[newword]=memo[item]+1
#                         temp.append(newword)
#                     else:
#                         if memo[newword]==0:
#                             del memo[newword]
#         if len(temp)==0:
#             return 0
#         words=temp
#     time3 = time.time()
#     print(time2-time1)
#     print(time3-time2)
#     return memo[endWord]
#
# ladderLength(beginWord,endWord,wordList)

