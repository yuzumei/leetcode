class Solution:
    def minPairSum(self, nums) -> int:
        nums.sort()
        n = len(nums)//2
        ans = 0
        for i in range(n):
            ans = max(ans, nums[i]+nums[len(nums)-i])
        return ans