class Solution:
    def maxIceCream(self, costs, coins: int) -> int:
        costs.sort()
        cnt,ans=0,0
        for cost in costs:
            if ans+cost>coins:
                return cnt
            ans+=cost
            cnt+=1
        return cnt