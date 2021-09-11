def x():
    nums =[]
    target = 4
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            ansleft=mid
            ansright=mid
            while ansleft>=0 and nums[ansleft]==target:
                ansleft-=1
            while ansright<=len(nums)-1 and nums[ansright]==target:
                ansright+=1
            return [ansleft+1,ansright-1]
        if nums[mid]<target:
            left=mid+1
        elif nums[mid]>target:
            right=mid-1
    return [-1,-1]
print(x())