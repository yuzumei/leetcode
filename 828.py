s = "LEETCODE"
'''dp[i]为到第i位的cnt'''
n=len(s)
import collections
memo=collections.defaultdict(list)
for i in range(n):
    memo[s[i]].append(i)
cnt=0
for item in memo:
    memo[item].insert(0,-1)
    memo[item].append(n)
    for i in range(1,len(memo[item])-1):
        left=memo[item][i]-memo[item][i-1]
        right=memo[item][i+1]-memo[item][i]
        cnt+=left*right
print(cnt)