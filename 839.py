class UF:
    def __init__(self,strlist):
        n=len(strlist)
        self.parent={i:i for i in range(n)}
        self.count=n

    def find(self,x):
        if self.parent[x]==x:
            return x
        else:
            self.parent[x]=self.find(self.parent[x])
            return self.parent[x]

    def union(self,x,y):
        if self.find(x)==self.find(y):
            return
        else:
            self.parent[self.find(x)]=self.find(y)
            self.count-=1

strs = ["tars","rats","arts","star"]
n=len(strs)
m=len(strs[0])
uf=UF(strs)
for i in range(n-1):
    for j in range(i+1,n):
        count=0
        for k in range(m):
            if strs[i][k]!=strs[j][k]:
                count+=1
            if count>2:
                break
        if count==2 or count==0:
            uf.union(i,j)
print(uf.count)
