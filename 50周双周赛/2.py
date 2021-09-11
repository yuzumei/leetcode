class Solution:
    def countPoints(self, points, queries):
        n=len(queries)
        ans=[0]*n
        for i in range(n):
            a,b,c=queries[i][0],queries[i][1],queries[i][2]*queries[i][2]
            for x in points:
                if (x[0]-a)*(x[0]-a)+(x[1]-b)*(x[1]-b)<=c:
                    ans[i]+=1
        return ans
x=Solution()
print(x.countPoints(points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]))