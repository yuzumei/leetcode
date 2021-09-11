s = "102351012345120012"
'''dp[i]表示到第i位的值算上第i位'''
if len(s)==0:
    return 0
if len(s)==1:
    return 0 if s[0]=="0" else 1
dp=[0]*len(s)
dp[0]=0 if s[0]=="0" else 1
if s[0] == '0':
    dp[1]=0
elif s[0] == '1':
    dp[1]=1 if s[1] == '0' else 2
elif s[0] == '2':
    dp[1]=2 if s[1] in ('1', '2', '3', '4', '5', '6') else 1
else:
    dp[1]=1 if s[1] != '0' else 0
if len(s)>2:
    for i in range(2,len(s)):
        tempstr=s[:i+1]
        if tempstr[-1]=="0":
            if tempstr[-2] in ('1','2'):
                dp[i]=dp[i-2]
            else:
                dp[i]=0
        if tempstr[-1] in ('1','2','3','4','5','6'):
            if tempstr[-2] in ('1','2'):
                dp[i]=dp[i-1]+dp[i-2]
            else:
                dp[i]=dp[i-1]
        if tempstr[-1] in ('7','8','9'):
            if tempstr[-2]=='1':
                dp[i]=dp[i-1]+dp[i-2]
            else:
                dp[i]=dp[i-1]
print(dp)
