class Solution:
    def maxAscendingSum(self, nums) -> int:
        ans=0
        temp=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                temp+=nums[i]
            else:
                ans=max(ans,temp)
                temp=nums[i]
        return max(ans,temp)