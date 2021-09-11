arr = [1,2,3,4,5,10,6,7,8,9]
k = 5
from collections import defaultdict
memo=defaultdict(int)
for item in arr:
    memo[item%5]+=1
if memo[0]%2!=0:
    return False
if k%2==0:
    for i in range(1,(k+1)/2):
        if memo[i]!=memo[k-i]:
            return False
    return True
else:
    if memo[k/2]%2!=0:
        return False
    for i in range(1,k/2):
        if memo[i] != memo[k - i]:
            return False
    return True