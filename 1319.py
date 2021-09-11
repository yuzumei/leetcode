class UF:
    def __init__(self,n):
        self.root={i:i for i in range(n)}
        self.diff=n-1
        self.remain=0

    def search(self,x):
        if self.root[x]==x:
            return x
        self.root[x]=self.search(self.root[x])
        return self.root[x]

    def match(self,conn):
        a=conn[0]
        b=conn[1]
        if self.root[self.search(a)]==self.root[self.search(b)]:
            self.remain+=1
            return
        self.root[self.search(b)]=self.root[self.search(a)]
        self.diff-=1

class Solution:
    def makeConnected(self, n: int, connections) -> int:
        uf=UF(n)
        for connection in connections:
            uf.match(connection)
            print(uf.remain,uf.diff)
        return uf.diff if uf.diff<=uf.remain else -1

x=Solution()
print(x.makeConnected(n = 12, connections = [[1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]]))
