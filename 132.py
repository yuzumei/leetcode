s='cddfadsfdsf'
dp=[0]*len(s)
'''dp[i]为包含第i位的最小分割点'''
dp[0]=0
for i in range(1,len(s)):
    dp[i]=dp[i-1]+1
    if s[:i+1]==s[:i+1][::-1]:
        dp[i]=0
    else:
        for j in range(1,i):
            if s[j:i+1]==s[j:i+1][::-1]:
                dp[i]=min(dp[i],dp[j-1]+1)
print(dp)