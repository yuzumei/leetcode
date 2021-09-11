class Solution:
    def findingUsersActiveMinutes(self, logs, k: int):
        import collections
        memo=collections.defaultdict(set)
        ans=[0]*(k+1)
        for log in logs:
            n=len(memo[log[0]])
            if log[1] not in memo[log[0]]:
                if ans[n]!=0:
                    ans[n] -= 1
                ans[n+1]+=1
                memo[log[0]].add(log[1])
        return ans[1:]

x=Solution()
print(x.findingUsersActiveMinutes(logs = [[1,1],[2,2],[2,3]], k = 4))