piles = [2,7,9,4,4,6,6,2,1,8,6,13,4,1,7,9,3,5,5,1,6]
"""1 <= X <= 2M。然后，令 M = max(M, X)"""
'''dp[n]表示有n堆时的最大石子数'''
n, memo = len(piles), dict()
# s[i] 表示第 i 堆石子到最后一堆石子的总石子数
s = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    s[i] = s[i + 1] + piles[i]
def dfs(i,m):
    if i>=n:
        return 0
    if (i,m) in memo:
        return memo[(i,m)]
    if i + m * 2 >= n:
        return s[i]
    best=0
    for x in range(1,1+2*m):
        best=max(best,s[i]-dfs(i+x,max(x,m)))
    memo[(i,m)]=best
    return best

return dfs(0,1)