def find():
    nums = [1,2,1,3,5,6,4]
    left=0
    right=len(nums)-1
    while left<right:
        mid=(left+right)//2
        if nums[mid]<nums[mid+1]:
            left=mid+1
        else:
            right=mid
    return right