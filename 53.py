nums = [-2]
ans=-float('inf')
temp=0
for item in nums:
    if item<0:
        ans=max(ans,item)
        temp+=item
        temp=max(0,temp)
    else:
        temp+=item
        ans=max(ans,temp)
print(ans)
