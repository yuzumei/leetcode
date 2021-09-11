nums=[1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1]
cnt=0
ans=0
for i in range(len(nums)):
    if nums[i]==1:
        cnt+=1
    else:
        ans=max(cnt,ans)
        cnt=0
return max(ans,cnt)