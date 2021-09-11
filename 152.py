nums=[2,3,-2,0,4,-5]
ans=-float('inf')
wait=0
temp=1
flag=0
for num in nums:
    if num==0:
        ans=max(ans,temp)
        temp=1
        wait=0
        flag=0
    elif num>0:
        temp*=num
    else:
        if flag==0:
            wait=temp
            flag=num
            temp=1
        else:
            temp=wait*flag*temp*num
            wait=0
            flag=0
    ans=max(ans,wait,temp)
print(ans)
        if not nums: return
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res
