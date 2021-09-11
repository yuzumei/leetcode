times = [[1,2,1]]
n = 2
k = 2
class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        import collections
        outdegree=collections.defaultdict(list)
        for item in times:
            outdegree[item[0]].append([item[1],item[2]])
        memo=[float('inf')]*(n+1)
        memo[k]=0
        res=[k]
        while res:
            temp=res.pop(0)
            for item in outdegree[temp]:
                target=item[0]
                dis=item[1]
                if memo[temp]+dis<memo[target]:
                    memo[target]=memo[temp]+dis
                    res.append(target)
        memo.pop(0)
        if max(memo)==float('inf'):
            return -1
        else:
            return max(memo)
x=Solution()
print(x.networkDelayTime(times,n,k))
