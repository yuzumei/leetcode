grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

class UF:
  def __init__(self,grid):
    self.parent={}
    self.count=0
    m=len(grid)
    n=len(grid[0])
    for row in range(m):
      for col in range(n):
        if grid[row][col] == '1':
          self.parent[row*n+col]=row*n+col
          self.count+=1
        else:
          self.parent[row * n + col]=-1

  def find(self,x):
    if x!=self.parent[x]:
      self.parent[x]=self.find(self.parent[x])
      return self.parent[x]
    return x

  def union(self,x,y):
    if self.find(x)==self.find(y):
      return
    else:
      self.parent[self.find(x)]=self.find(y)
      self.count-=1

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    row=len(grid)
    if row==0:
      return 0
    col=len(grid[0])
    uf=UF(grid)
    for r in range(row):
      for c in range(col):
        if grid[r][c]=="1":
          for (x,y) in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if x>=0 and x<=row-1 and y>=0 and y<=col-1 and grid[x][y]=="1":
              uf.union(col*r+c,col*x+y)
    return uf.count



# def union(self, x, y):
#   rootx = self.find(x)
#   rooty = self.find(y)
#   if rootx != rooty:
#     if self.rank[rootx] < self.rank[rooty]:
#       rootx, rooty = rooty, rootx
#     self.parent[rooty] = rootx
#     if self.rank[rootx] == self.rank[rooty]:
#       self.rank[rootx] += 1
#     self.count -= 1

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    nr = len(grid)
    if nr == 0:
      return 0
    nc = len(grid[0])

    uf = UnionFind(grid)
    num_islands = 0
    for r in range(nr):
      for c in range(nc):
        if grid[r][c] == "1":
          grid[r][c] = "0"
          for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
              uf.union(r * nc + c, x * nc + y)

    return uf.getCount()



