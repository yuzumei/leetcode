class Solution:
    def maxSumSubmatrix(self, matrix, k: int) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[[] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=[matrix[k][i] for k in range(m)]
                else:
                    dp[i][j]=[dp[i][j-1][k]+matrix[k][j] for k in range(m)]
        ans=-float('inf')
        for i in range(n):
            for j in range(i,n):
                temp=[0]*m
                for s in range(m):
                    temp[s]=max(temp[s-1],0)+dp[i][j][s]
                    if 0<temp[s]<=k:
                        ans=max(temp[s],ans)
                    if ans==k:
                        return k
        print(dp)
        return ans if ans>0 else -1
matrix = [[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]]
k = 8
x=Solution()
print(x.maxSumSubmatrix(matrix,k))

