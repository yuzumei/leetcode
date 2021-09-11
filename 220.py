class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        if k==0:
            return False
        memo=[]
        cnt=0
        for num in nums:
            if cnt>k:
                memo.pop(0)
            if memo[num]!=0:
                return True
            for i in range(-t,t+1):
                memo[num+i]+=1
            cnt+=1
        return False

x=Solution()
print(x.containsNearbyAlmostDuplicate(nums = [1,0,1,1], k = 1, t = 2))