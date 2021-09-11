strs=["eat", "tea", "tan", "ate", "nat", "bat"]
alpha='qwertyuiopasdfghjklzxcvbnm'
num=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,73,79,83,89,93,97,101]
comb={alpha[i]:num[i] for i in range(26)}
import collections
memo=collections.defaultdict(list)
ans=[]
for word in strs:
    temp=1
    for i in word:
        temp*=comb[i]
    memo[temp].append(word)
for item in memo:
    ans.append(memo[item])