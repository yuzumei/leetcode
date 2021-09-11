startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]
n=len(startTime)
all=[[startTime[i],endTime[i],profit[i]] for i in range(n)]
all=sorted(all,key=lambda x:x[1])
end=max(endTime)
dp=[0 for i in range(end+1)]
ans=0
'''dp[i]是到i时间的最大收入'''
for i in range(1,end+1):
    dp[i]=dp[i-1]
    for j in range(ans,n):
        temp=all[j]
        if temp[1]==i:
            dp[i]=max(dp[temp[0]]+temp[2],dp[i])
        if temp[1]>i:
            ans=j
            break
print(dp[end])
