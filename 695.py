grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

class UF:
    def __init__(self,n):
        self.parent={i:i for i in range(n)}

    def find(self,x):
        if self.parent[x]==x:
            return x
        else:
            self.parent[x]=self.find(self.parent[x])
            return self.parent[x]

    def union(self,x,y):
        if self.parent[self.find(x)]==self.parent[self.find(y)]:
            return
        else:
            self.parent[self.find(y)]=self.find(x)

n=len(grid)
m=len(grid[0])
uf=UF(n*m)
from collections import defaultdict
ans=defaultdict(int)
for i in range(n):
    for j in range(m):
        if grid[i][j]==1:
            if i!=n-1:
                if grid[i+1][j]==1:
                    uf.union(j*n+i,j*n+i+1)
            if j!=m-1:
                if grid[i][j+1]==1:
                    uf.union(j*n+i,(j+1)*n+i)
print(uf.parent)
for i in range(n):
    for j in range(m):
        if grid[i][j]==1:
            ans[uf.find(j*n+i)]+=1
print(max(list(ans.values())))

