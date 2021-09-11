matrix = [[1,2,3],[4,5,6],[7,8,9]]
n=len(matrix)
ans=[[matrix[i][j] for i in range(n)][::-1] for j in range(n)]
print(ans)