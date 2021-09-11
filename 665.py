nums = [4,2,3]
newnums=[-float('inf')]+nums
cnt=0
for i in range(1,len(newnums)):
    if newnums[i]<newnums[i-1]:
        if newnums[i]<newnums[i-2]:
            newnums[i]=newnums[i-1]
        cnt+=1
    if cnt==2:
        return False
return True