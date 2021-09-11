class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        #相邻坐标（r,c）的和，奇偶性不同。 所以转化为二部图，求增广路径（折过来，着过去，W型路线）
        Row, Col = n, m

        match = [[None for _ in range(Col)] for _ in range(Row)]
        for r, c in broken:
            match[r][c] = '#'           #这个点不能被匹配

        def dfs(r: int, c: int, visited: set()) -> bool:        #find增广路径  模板 visit直接在参数里传递了
            visited.add((r, c))
            for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)): #有连接的边
                if 0<= nr < Row and 0<= nc < Col:               #有连接的边
                    nxt = match[nr][nc]     #寻找增广路径

                    if nxt in visited:      #没访问过，且不是坑（坑已经在visited里面了）
                        continue
                    if nxt == None or dfs(nxt[0], nxt[1], visited) == True: #如果还没配对，或者配的对可以找到增广路径
                        match[r][c] = (nr, nc)
                        match[nr][nc] = (r, c)
                        return True
            return False

        res = 0
        for r in range(Row):
            for c in range(Col):
                if (r + c) % 2 == 0:            #从偶集开始，从奇数集开始也行
                    if (match[r][c] != '#'):
                        if dfs(r, c, {'#'}) == True:
                            res += 1
        return res
x=Solution()
print(x.domino(n = 2, m = 3, broken = [[1, 1], [1, 2]]))