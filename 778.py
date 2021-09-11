grid=[[7,23,21,9,5],[3,20,8,18,15],[14,13,1,0,22],[2,10,24,17,12],[6,16,19,4,11]]
# 输出: 16
class UF():
    def __init__(self,n):
        self.parent={i:i for i in range(n)}

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
            return self.parent[x]
        return x

    def union(self,x,y):
        if self.find(x)==self.find(y):
            return
        else:
            self.parent[self.find(x)]=self.find(y)

    def test(self,x,y):
        return self.find(x)!=self.find(y)

from collections import defaultdict
n=len(grid)
m=len(grid[0])
uf=UF(n*m)
memo=defaultdict(list)
for i in range(n):
    for j in range(m):
        memo[grid[i][j]].append([i,j])

t=0
while uf.test(0,n*m-1):
    for item in memo[t]:
        row=item[0]
        col=item[1]
        if row!=0:
            if grid[row-1][col]<=t:
                uf.union(row+col*n,row-1+col*n)
        if row != n-1:
            if grid[row + 1][col] <= t:
                uf.union(row + col * n, row + 1 + col * n)
        if col!=0:
            if grid[row][col-1]<=t:
                uf.union(row+col*n,row+(col-1)*n)
        if col != m-1:
            if grid[row][col+1] <= t:
                uf.union(row + col * n, row + (col+1) * n)
    print(uf.parent)
    t+=1
print(t-1)



