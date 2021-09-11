cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
'''cost[i][j]是第一组的i和第二组的j'''
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m,n=len(cost),len(cost[0])
        mi=[min(cost[i][j] for i in range(m)) for j in range(n)]#预处理第二组每个点的最小cost
        @lru_cache(None)
        def dp(i,used):
            if i==m:#第一组点全部选完后，处理第二组还没选的点的最小成本和
                ans=0
                for j in range(n):
                    if not 1<<j&used:#如果第二组这个点没被选过，那么就选它在第一组中最小代价点
                        ans+=mi[j]
                return ans
            res=inf
            for j in range(n):
                res=min(res,cost[i][j]+dp(i+1,used|1<<j))#转移方程
            return res
        return dp(0,0)
