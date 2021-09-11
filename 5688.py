word1 = "ceebeddc"
word2 = "d"
n=len(word1)+len(word2)
m=len(word1)
word=word1+word2
'''dp[i][j] word[i:j+1]'''
dp=[[0]*n for _ in range(n)]
ans=0
for i in range(n-1,-1,-1):
    for j in range(i,n):
        if i==j:
            dp[i][j]=1
        elif j==i+1:
            dp[i][j]=2 if word[i]==word[j] else 1
        else:
            dp[i][j]=2+dp[i+1][j-1] if word[i]==word[j] else max(dp[i+1][j],dp[i][j-1])
        if i<m and j>=m and word[i]==word[j]:
            ans=max(ans,dp[i][j])
print(ans)

