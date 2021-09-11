def x():
    nums = [2,3,3,2,4]
    left=0
    right=0
    maxnum=-float('inf')
    minnum=float('inf')
    for i,num in enumerate(nums):
        if num<maxnum:
            right=i
            minnum=min(minnum,num)
        maxnum=max(maxnum,num)
    if minnum==float('inf'):
        return 0
    while nums[left]<=minnum:
        left+=1
    return right-left+1
print(x())