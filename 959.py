'''并查集'''
class UF:
    def __init__(self,M):
        self.parent={}
        self.count=M
        for i in range(M):
            self.parent[i]=i

    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
            return self.parent[x]
        return x

    def union(self,x,y):
        if self.find(x)==self.find(y):
            return
        self.parent[self.find(x)]=self.find(y)
        self.count-=1

class Solution:
    def regionsBySlashes(self, grid):
        n=len(grid)
        N=4*n*n
        uf=UF(N)
        def transform(row,col,i):
            return (row*n+col)*4+i
        for row in range(n):
            for col in range(n):
                if row>0:
                    uf.union(transform(row-1,col,2),transform(row,col,1))
                if col>0:
                    uf.union(transform(row,col-1,3),transform(row,col,0))
                if grid[row][col]=='/':
                    uf.union(transform(row,col,0),transform(row,col,1))
                    uf.union(transform(row, col, 2), transform(row, col, 3))
                if grid[row][col]=='\\':
                    uf.union(transform(row,col,0),transform(row,col,2))
                    uf.union(transform(row, col, 1), transform(row, col, 3))
                if grid[row][col]=='':
                    uf.union(transform(row,col,0),transform(row,col,1))
                    uf.union(transform(row, col, 0), transform(row, col, 2))
                    uf.union(transform(row, col, 0), transform(row, col, 3))
        return uf.count
