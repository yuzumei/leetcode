matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
n=len(matrix)
m=len(matrix[0])
def twoside(heights):
    n = len(heights)
    if n == 0:
        return 0
    leftnum = [0] * n
    rightnum = [n] * n
    stack = []
    for i, num in enumerate(heights):
        while stack and num <= stack[-1][1]:
            temp = stack.pop()
            rightnum[temp[0]] = i
        leftnum[i] = stack[-1][0] if stack else -1
        stack.append([i, num])
    ans = max((rightnum[i] - leftnum[i] - 1) * heights[i] for i in range(n))
    return ans
memo=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if matrix[i][j]=="0":
            memo[i][j]=0
        else:
            if j==0:
                memo[i][0]=1
            else:
                memo[i][j]=memo[i][j-1]+1
ans=0
for i in range(m):
    temp=[memo[j][i] for j in range(n)]
    ans=max(ans,twoside(temp))
print(ans)