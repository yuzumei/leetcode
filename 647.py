s='aaaa'
n=len(s)
dp=[[0]*n for _ in range(n)]
ans=0
for i in range(n):
    for j in range(i+1):
        if i==j:
            dp[i][j]=1
        else:
            if s[i]!=s[j]:
                dp[i][j]=0
            else:
                dp[i][j]=1 if i-j==1 else dp[i-1][j+1]
        if dp[i][j]==1:
            ans += 1
print(dp)
