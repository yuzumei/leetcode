piles = [2,7,9,4,4,6,6,2,1,8,6,13,4,1,7,9,3,5,5,1,6]
"""1 <= X <= 2M。然后，令 M = max(M, X)"""
'''dp[n]表示有n堆时的最大石子数'''
n, memo = len(piles), dict()

# s[i] 表示第 i 堆石子到最后一堆石子的总石子数
s = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    s[i] = s[i + 1] + piles[i]


# dfs(i, M) 表示从第 i 堆石子开始取，最多能取 M 堆石子所能得到的最优值
def dfs(i, M):
    # 如果已经搜索过，直接返回
    if (i, M) in memo:
        return memo[(i, M)]
    # 溢出拿不到任何石子
    if i >= n:
        return 0
    # 如果剩余堆数小于等于 2M， 那么可以全拿走
    if i + M * 2 >= n:
        return s[i]
    # 枚举拿 x 堆的最优值
    best = 0
    for x in range(1, M * 2 + 1):
        # 剩余石子减去对方最优策略
        best = max(best, s[i] - dfs(i + x, max(x, M)))
    # 记忆化
    memo[(i, M)] = best
    print(memo)

    return best


print(dfs(0,1))
