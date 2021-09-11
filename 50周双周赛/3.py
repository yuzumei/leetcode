class Solution:
    def getMaximumXor(self, nums, maximumBit: int):
        n=len(nums)
        ans=[]
        s=2**maximumBit-1
        res=0
        for num in nums:
            res^=num
        for num in nums[::-1]:
            ans.append(res^s)
            res^=num
        return ans

x=Solution()
print(x.getMaximumXor(nums = [0,1,2,2,5,7], maximumBit = 3))