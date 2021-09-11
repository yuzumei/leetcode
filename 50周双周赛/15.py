class Solution:
    def closestRoom(self, r, q):
        n, m = len(r), len(q)
        ans = [-1] * m
        a = list(range(m))
        a.sort(key=lambda x: q[x][1])
        from sortedcontainers import SortedList
        sl = SortedList(r)
        print(sl)
        r.sort(key=lambda x: x[1])
        i = 0
        for j in a:
            while i < n and r[i][1] < q[j][1]:
                sl.remove(r[i])
                i += 1
            k = sl.bisect_left([q[j][0], 0])
            if len(sl) > k - 1 >= 0 and (k >= len(sl) or abs(sl[k - 1][0] - q[j][0]) <= abs(sl[k][0] - q[j][0])):
                k -= 1
            if 0 <= k < len(sl):
                ans[j] = sl[k][0]
            # print(r,i,sl,ans)
        return ans
x=Solution()
print(x.closestRoom(r = [[1,4],[2,3],[3,5],[4,1],[5,2]], q = [[2,3],[2,4],[2,5]]))