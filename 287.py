nums = [1,3,4,2,2]
for num in nums:
    if nums[abs(num)]<0:
        return abs(num)
    nums[abs(num)]=-nums[abs(num)]
