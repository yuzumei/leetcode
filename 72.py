word1 = "intention"
word2 = "execution"
n=len(word1)
m=len(word2)
dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if i==0:
            dp[i][j]=j
        elif j==0:
            dp[i][j]=i
        else:
            if word1[i-1]==word2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
print(dp)
