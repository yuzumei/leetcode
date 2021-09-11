nums = [1,2,3,1,1,3]
from collections import defaultdict
memo=defaultdict(int)
for item in nums:
    memo[item]+=1
ans=0
for item in memo:
    if memo[item]>=2:
        ans+=(memo[item])*(memo[item]-1)/2
print(int(ans))