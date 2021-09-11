s = "a"
t = "aa"
def match(a,b):
    for item in b:
        if a[item]<b[item]:
            return False
    return True
from collections import defaultdict
memot=defaultdict(int)
memos=defaultdict(int)
ans=float('inf')
for item in t:
    memot[item]=1
l,r=0,0
while r<=len(s):
    if match(memos,memot):
        ans=min(ans,r-l)
        res = s[l:r]
        # if ans==len(t):
        #     return ans
        memos[s[l]]-=1
        l+=1
    else:
        if r<len(s):
            memos[s[r]]+=1
        r+=1
print(res)