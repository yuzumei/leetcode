class Solution:
    def checkSubarraySum(self,nums,k):
        res=[0]*len(nums)
        if len(nums)<2:
            return False
        if k!=0:
            res[0]=nums[0]%k
            res[1]=(nums[0]+nums[1])%k
        else:
            res[0]=nums[0]
            res[1]=(nums[0]+nums[1])
        for i in range(1,len(nums)):
            if k!=0:
                ans=sum(nums[k] for k in range(i+1))%k
            else:
                ans=sum(nums[k] for k in range(i+1))
            res[i]=ans
            if ans in res[:i-1] or ans==0:
                return True
            print(res)
        return False
test=Solution()
print(test.checkSubarraySum([23,2,4,0,0],0))