nums = [0,3,7,2,5,8,4,6,0,1]
import collections
memo=collections.defaultdict(int)
for num in nums:
    memo[num]=1
    memo[num-1]=0 if memo[num-1]!=1 else 1
    memo[num+1]=0 if memo[num+1]!=1 else 1
ans=0
print(memo)
memo1=dict()
for item in memo:
    temp = 0
    if memo[item]==1:
        if item not in memo1:
            numleft=item
            numright=item
            while memo[numleft]==1:
                numleft-=1
                temp+=1
                memo1[numleft]=0
            while memo[numright]==1:
                numright+=1
                temp+=1
                memo1[numright]=0
        memo1[item] = 0
    ans=max(ans,temp-1)
print(ans)
