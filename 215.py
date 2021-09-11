nums=[3,2,1,5,6,4]
k = 2
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        import random
        random.shuffle(nums)
        def quicksearch(nums):
            print(nums)
            num=nums[0]
            left=[]
            right=[]
            for i in range(1,len(nums)):
                if nums[i]<num:
                    left.append(nums[i])
                else:
                    right.append(nums[i])
            return num,left,right
        num,left,right=quicksearch(nums)
        cnt=k-1
        while True:
            if len(right)==cnt:
                return num
            elif len(right)>cnt:
                num,left,right=quicksearch(right)
            else:
                cnt-=len(right)
                num, left, right = quicksearch(left+[num])
x=Solution()
print(x.findKthLargest(nums,k))

