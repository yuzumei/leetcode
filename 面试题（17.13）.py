dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
class Trie:
    def __init__(self,words):
        self.root={}
        self.length=0
        for word in words:
            self.length=max(self.length,len(word))
            node=self.root
            for c in word:
                if c not in node:
                    node[c]={}
                node=node[c]
            node["leaf"]=word

    def serach(self,word):
        node=self.root
        for c in word:
            if c not in node:
                return 0
            node=node[c]
        if "leaf" in node:
            return 1

trie=Trie(dictionary)
n=trie.length
'''dp[i]表示到第i个字符（不包括i）'''
dp=[0]*(len(sentence)+1)
for i in range(1,len(sentence)+1):
    tempdp=dp[i-1]+1
    for j in range(max(0,i-n),i):
        temp=sentence[j:i]
        if trie.serach(temp):
            tempdp=min(tempdp,dp[j])
    dp[i]=tempdp
print(dp)


