class Trie:
    def __init__(self,words):
        self.root={}
        for word in words:
            temp=self.root
            for c in word:
                if c not in temp:
                    temp[c]={}
                temp=temp[c]
            temp["leaf"]=word

    def search(self,s):
        ans=[]
        temp=self.root
        for c in s:
            if c in temp:
                temp=temp[c]
            else:
                break
            if "leaf" in temp:
                ans.append(temp["leaf"])

        return ans

from collections import defaultdict

class Solution:
    def multiSearch(self,big,smalls):
        trie=Trie(smalls)
        bigdict=defaultdict(list)

        for i in range(len(big)):
            res=trie.search(big[i:])
            for item in res:
                bigdict[item].append(i)

        res=[]
        for item in smalls:
            res.append(bigdict[item])

        return res