class Solution:
    def maxBuilding(self, n: int, restrictions) -> int:
        if not restrictions:
            return n-1
        def calc(a,b):
            return (a[0]+a[1]-b[0]-b[1])//2
        restrictions.sort(key=lambda x:x[0])
        stack=[[1,0]]
        ans=0
        for item in restrictions:
            item[1]=min(item[1],item[0]-1,stack[-1][1]-stack[-1][0]+item[0])
            if len(stack)==1:
                stack.append(item)
            else:
                while len(stack)>1 and item[0]-stack[-1][0]<stack[-1][1]-item[1]:
                    stack.pop()
                stack.append(item)
        print(stack)
        temp=stack.pop(0)
        while stack:
            new=stack.pop(0)
            ans=max(ans,calc(new,temp)+temp[1])
            temp=new
        newans=temp[1]+n-1-temp[0]
        return max(ans,newans)
x=Solution()
print(x.maxBuilding(n = 10, restrictions = [[6,0],[5,2],[7,0],[9,1],[2,4],[3,4],[4,0],[8,2],[10,0]]))
print(x.maxBuilding(n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]))
print(x.maxBuilding(100,[[68,36],[25,30],[81,2],[7,26],[63,35],[83,33],[36,22],[21,50],[13,27],[57,50],[100,35],[92,9],[89,27],[29,39],[9,3],[37,22],[98,5],[18,38],[87,30],[67,43],[71,15],[45,20],[97,21],[46,15],[24,17],[17,10],[90,12],[41,0],[79,3],[77,42],[61,29],[69,21],[53,8],[64,45],[6,2],[51,21],[40,5],[93,30],[99,12],[32,36],[5,36],[26,34],[2,35],[20,24],[66,45],[12,15],[96,10],[52,19],[19,9],[14,47],[74,25],[56,39],[82,27],[86,42],[33,47],[88,38],[70,48],[91,11],[73,33],[31,8],[85,21],[8,50],[65,0],[78,36],[11,3],[27,0],[16,4],[49,30],[10,42],[76,32],[35,0],[60,45],[39,39],[43,25],[15,39],[84,15],[75,45],[54,9],[80,7],[58,4],[55,43],[30,8],[38,48],[22,40],[47,24],[62,12],[59,33],[48,12],[50,9],[28,30],[34,19],[4,19],[95,26],[72,12],[3,46],[94,25],[44,32],[42,48],[23,48]]))