def find():
    nums = [4,5,6,7,0,1,2]
    target = 0
    if not nums:
        return -1
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        if nums[0]<=nums[mid]:
            if
print(find())
