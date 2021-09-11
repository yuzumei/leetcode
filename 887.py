class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        '''f(t,k)=1+f(t-1,k-1)+f(t-1,k)'''
        f=[[0]*(K+1) for _ in range(N+1)]
        for t in range(N + 1):
            for k in range(K+1):
                if k==0 or t==0:
                    f[t][k]=0
                else:
                    f[t][k]=1+f[t-1][k]+f[t-1][k-1]
                if f[t][k]>=N:
                    return t
        dp=[[1]*(K+1) for _ in range(N+1)]
        # for i in range(1,N+1):
        #     for k in range(1,K+1):
        #         if k==1:
        #             dp[i][k]=i
        #         else:
        #             if i>1:
        #                 temp=max(dp[i-2][k],dp[1][k-1])
        #                 for j in range(k,i):
        #                     if max(dp[i-j-1][k],dp[j][k-1])>temp:
        #                         break
        #                     else:
        #                         temp=max(dp[i-j-1][k],dp[j][k-1])
        #                 dp[i][k]=temp+1
        # return dp[-1][-1]
x=Solution()
print(x.superEggDrop(1,2))
print(x.superEggDrop(2,1))
print(x.superEggDrop(3,14))
print(x.superEggDrop(2,6))
print(x.superEggDrop(4,5000))