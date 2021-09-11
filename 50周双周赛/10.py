class Solution:
    def maxFrequency(self, nums, k: int) -> int:
        nums.sort()
        ans,memo=0,0
        queue=[]
        for num in nums:
            if not queue:
                queue.append(num)
            else:
                temp=num-queue[-1]
                memo+=(temp*len(queue))
                while queue and memo>k:
                    s=queue.pop(0)
                    memo-=(num-s)
                queue.append(num)
            ans=max(ans,len(queue))
        return ans
x=Solution()
print(x.maxFrequency(nums = [3], k = 2))