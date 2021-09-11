nums = [1,3,5,4,7]
count=1
ans=1
tempmax=nums[0]
for item in nums[1:]:
    if item>tempmax:
        count+=1
        ans = max(count, ans)
    else:
        count=1
    tempmax = item
print(ans)