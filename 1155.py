d = 1 #筛子数目
f = 6 #筛子面
target = 3    #总和
'''dp[i][k]表示i个筛子投到k和'''
dp=[[0]*(target+1) for i in range(d+1)]
for i in range(1,min(target+1,f+1)):
    dp[1][i]=1
for i in range(2,d+1):
    for k in range(i,min(target+1,f*i+1)):
        temp=0
        for s in range(max(1, k - f), k):
            temp=temp+dp[i-1][s]
            dp[i][k]=temp%(1e9 + 7)
print(dp[d][target])