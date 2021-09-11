queries = [[2,6],[5,1],[73,660]]
from collections import defaultdict
def prime(a):
    res=defaultdict(int)
    i=2
    while a>1:
        if a%i==0:
            a=a/i
            res[i]+=1
        else:
            i=i+1 if i%2==0 else i+2
    return res
import math
res=[]
for query in queries:
    if query[1]==1:
        res.append(1)
    else:
        x=prime(query[1])
        ans=1
        for item in x:
            ans*=(math.comb(query[0]+x[item]-1,x[item]))
            ans=ans%(10**9+7)
        res.append(ans)
print(res)
