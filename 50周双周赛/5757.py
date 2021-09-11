class Solution:
    def getBiggestThree(self, grid):
        m,n = len(grid),len(grid[0])
        def get_len(x,y):
            return min(x,n-1-y,y,m-1-x)
        def get_ans(i,j,s):
            res = grid[i-s][j] + grid[i+s][j] + grid[i][j-s] +grid[i][j+s]
            for l in range(1,s):
                res += (grid[i+l][j+s-l] + grid[i-l][j+s-l] + grid[i+l][j+l-s] + grid[i-l][j+l-s])
            return res
        ans = set()
        for i in range(m):
            for j in range(n):
                num = get_len(i,j)
                ans.add(grid[i][j])
                if num >= 1:
                    for s in range(1,num+1):
                        res = get_ans(i,j,s)
                        ans.add(res)
                        while len(ans)>3:
                            temp = min(ans)
                            ans.remove(temp)
                while len(ans)>3:
                    temp = min(ans)
                    ans.remove(temp)
        return sorted(list(ans),reverse=True)

grid = [[20,17,9,13,5,2,9,1,5],[14,9,9,9,16,18,3,4,12],[18,15,10,20,19,20,15,12,11],[19,16,19,18,8,13,15,14,11],[4,19,5,2,19,17,7,2,2]]
x=Solution()
print(x.getBiggestThree(grid))