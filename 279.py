import math
n=88
nums=[i*i for i in range(1,int(math.sqrt(n))+1)]
from collections import defaultdict
memo=defaultdict(int)
memo[n]=0
queue=[n]
while memo[0]==0:
    num=queue.pop(0)
    for i in nums:
        if num-i>=0 and memo[num-i]==0:
            memo[num-i]=memo[num]+1
            queue.append(num-i)
print(memo[0])
