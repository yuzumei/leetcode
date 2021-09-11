nums=[1,2,2,3,1,4,2]
import collections
memo=collections.defaultdict(list)
for i,item in enumerate(nums):
    memo[item].append(i)
maxlength=1
ans=len(nums)
for item in memo:
    if len(memo[item])==maxlength:
        ans=min(ans,memo[item][-1]-memo[item][0]+1)
    elif len(memo[item])>maxlength:
        ans = len(nums)
        ans = min(ans, memo[item][-1] - memo[item][0] + 1)
        maxlength=len(memo[item])
print(ans)