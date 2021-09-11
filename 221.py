matrix = [["0","0","0","0","1","1","1","0","1"],["0","0","1","1","1","1","1","0","1"],["0","0","0","1","1","1","1","1","0"]]
n=len(matrix)
m=len(matrix[0])
memo=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if matrix[i][j]=='1':
            memo[i][j]=memo[i][j-1]+1 if j!=0 else 1
        else:
            memo[i][j]=0
print(memo)
ans=0
for i in range(m):
    temp=[memo[j][i] for j in range(n)]
    stack=[]
    for num in temp:
        if not stack or num>=stack[-1]:
            stack.append(num)
        else:
            for i in range(len(stack)-1,-1,-1):
                if stack[i]<num:
                    break
                stack[i]=num
            stack.append(num)
        while stack and stack[0]<=len(stack):
            res=stack.pop(0)
            ans=max(ans,res*res)
print(ans)
