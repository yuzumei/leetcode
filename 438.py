s="abab"
p="ab"
n=len(s)
k=len(p)
from collections import defaultdict
test=defaultdict(int)
memo=defaultdict(int)
for item in p:
    test[item]+=1
left=0
right=k
ans=[]
for item in s[:k]:
    memo[item]+=1
while right<=n:
    if memo == test:
        ans.append(left)
    if right!=n:
        memo[s[left]] -= 1
        memo[s[right]] += 1
    if memo[s[left]] == 0:
        del memo[s[left]]
    left += 1
    right += 1
    print(memo)
print(ans)