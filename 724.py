nums = [1, 7, 3, 6, 5, 6]
ans=-1
if len(nums)<=2:
    return 0
leftstart=nums[0]
rightstart=sum(nums[2:])
if leftstart==rightstart:
    return 0
for i in range(1,len(nums)-1):
    leftstart+=nums[i]
    rightstart-=nums[i+1]
    if leftstart==rightstart:
        return i
return -1