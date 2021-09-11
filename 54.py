matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
class Solution:
    def spiralOrder(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        newmatrix=[[-101]*(m+2)]
        for i in range(n):
            newmatrix.append([-101]+matrix[i]+[-101])
        newmatrix.append([-101]*(m+2))
        ans=[]
        start=[1,1]
        direct=[(0,1),(1,0),(0,-1),(-1,0)]
        i=0
        while len(ans)!=m*n:
            ans.append(newmatrix[start[0]][start[1]])
            newmatrix[start[0]][start[1]]=-101
            if newmatrix[start[0]+direct[i][0]][start[1]+direct[i][1]]==-101:
                i+=1
                i=i%4
            start=[start[0]+direct[i][0],start[1]+direct[i][1]]
        return ans

x=Solution()
print(x.spiralOrder(matrix))