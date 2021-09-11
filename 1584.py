class UF:
    def __init__(self,n):
        self.parent={i:i for i in range(n)}
        self.flag=0
        self.count=n

    def find(self,x):
        if self.parent[x]==x:
            return x
        else:
            self.parent[x]=self.find(self.parent[x])
            return self.parent[x]

    def union(self,x,y):
        if self.find(x)==self.find(y):
            self.flag = 0
            return
        else:
            self.parent[self.find(x)]=self.find(y)
            self.count-=1
            self.flag = 1

def find():
    points = [[2,-3],[-17,-8],[13,8],[-17,-15]]
    n=len(points)
    uf=UF(n)
    from collections import defaultdict
    memo=defaultdict(list)
    length=set()
    for i in range(n):
        for j in range(i+1,n):
            temp=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
            memo[temp].append([i,j])
            length.add(temp)
    lengthlist=sorted(list(length))
    ans=0
    for length in lengthlist:
        for item in memo[length]:
            uf.union(item[0],item[1])
            if uf.flag==1:
                ans+=length
            if uf.count==1:
                return ans

print(find())