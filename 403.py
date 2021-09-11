class Solution:
    def canCross(self, stones) -> bool:
        if stones[1]!=1:
            return False
        memo=dict()
        for stone in stones:
            memo[stone]=1
        bfs=[[1,1]]
        while bfs:
            x=bfs.pop(0)
            print(len(bfs))
            for step in (x[1]-1,x[1],x[1]+1):
                if step>0 and step+x[0] in memo:
                    bfs.append([step+x[0],step])
                    if step+x[0]==stones[-1]:
                        return True
        return False

s=list(range(2000))
s.sort(re)
x=Solution()
print(x.canCross(stones = s))

