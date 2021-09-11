nums = [35,13,1,4,31,3,4,31,3,46,7,3,13,46,4,31,34,2,13,43,9,13,1,34,31,34,63,43,5,9,7,7,1,3,46,3,13,5]
k = 3
class Solution:
    def minChanges(self, nums, k: int) -> int:
        if k==1:
            ans=0
            for num in nums:
                if num!=0:
                    ans+=1
            return ans
        dp=[[0]*1024 for _ in range(k)]
        import collections
        memo=[collections.defaultdict(int) for _ in range(k)]
        cnt=[set() for _ in range(k)]
        cnt1=[0]*k
        for i,num in enumerate(nums):
            memo[i%k][num]+=1
            cnt1[i%k]+=1
            cnt[i%k].add(num)
        for i in range(k):
            if i!=0:
                tempmin=min(dp[i-1][l] for l in range(1024))
            for v in range(1024):
                if i==0:
                    dp[i][v]=cnt1[i]-memo[i][v]
                else:
                    dp[i][v] = tempmin + cnt1[i]
                    for s in cnt[i]:
                        dp[i][v]=min(dp[i-1][v^s]+cnt1[i]-memo[i][s],dp[i][v])
        return dp[-1][0]
x=Solution()
print(x.minChanges(nums,k))
