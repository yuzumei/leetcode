grid = [[1,3,1],[1,5,1],[4,2,1]]
m =len(grid)
n =len(grid[0])
ans=[[float('inf')]*n for _ in range(m)]
ans[0][0]=grid[0][0]
queue=[0]
while len(queue)!=0:
    nums=queue.pop(0)
    x=nums//n
    y=nums-x*n
    if x<m-1:
        ans[x+1][y]=min(ans[x+1][y],ans[x][y]+grid[x+1][y])
        if (x+1)*n+y not in queue:
            queue.append((x+1)*n+y)
    if y<n-1:
        ans[x][y+1]=min(ans[x][y+1],ans[x][y]+grid[x][y+1])
        if x*n+y+1 not in queue:
            queue.append(x*n+y+1)
print(ans[-1][-1])