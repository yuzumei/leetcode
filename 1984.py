class Solution:
    def minimumDifference(self, nums, k: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums) - k):
            ans = min(ans, nums[i + k] - nums[i])
        return ans