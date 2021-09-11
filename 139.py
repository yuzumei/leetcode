s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a", "aa"]
class Trie:
    def __init__(self,words):
        self.root={}
        self.maxlength=0
        for word in words:
            self.maxlength=max(self.maxlength,len(word))
            temp = self.root
            for c in word:
                if c not in temp:
                    temp[c]={}
                temp=temp[c]
            temp['leaf']=word

    def search(self,s):
        temp=self.root
        for c in s:
            if c in temp:
                temp=temp[c]
            else:
                return False
        return 'leaf' in temp

trie=Trie(wordDict)
print(trie.root)
n=trie.maxlength
dp=[False]*(len(s)+1)
queue=[0]
for i in range(1,len(s)+1):
    if queue[-1]-queue[0]>=n:
        queue.pop(0)
    for start in queue:
        dp[i]|=trie.search(s[start:i])
    if dp[i]:
        queue.append(i)
print(dp)






# def find():
#     for item in set(s):
#         if item not in trie.alpha:
#             return False
#     queue = [s]
#     while queue:
#         item=queue.pop()
#         if len(item)==0:
#             return True
#         temp=trie.root
#         for i in range(len(item)):
#             if item[i] in temp:
#                 temp=temp[item[i]]
#                 if 'leaf' in temp:
#                     queue.append(item[i+1:])
#             else:
#                 break
#     return False
# print(find())
# def dfs(target):
#     global flag
#     if len(target)==0:
#         print('2')
#         flag=1
#         return True
#     temp = trie.root
#     for i in range(len(target)):
#         if target[i] in temp:
#             temp=temp[target[i]]
#             if 'leaf' in temp:
#                 dfs(target[i+1:])
#         else:
#             break
#     return flag==1
# print(dfs(s))

