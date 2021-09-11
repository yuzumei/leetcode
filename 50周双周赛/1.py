class Solution:
    def minOperations(self, nums) -> int:
        cnt=0
        memo=0
        for num in nums:
            if num<=memo:
                cnt+=(memo+1-num)
            memo=max(num,memo+1)
        return cnt

x=Solution()
print(x.minOperations([8]))