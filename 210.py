n,pre=4,[[1,0],[2,0],[3,1],[3,2]]
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        import collections
        memo=collections.defaultdict(list)
        indeg=collections.defaultdict(int)
        ans=[]
        stack=[]
        for prerequisite in prerequisites:
            memo[prerequisite[1]].append(prerequisite[0])
            indeg[prerequisite[1]]+=0
            indeg[prerequisite[0]]+=1
        for item in indeg:
            if indeg[item]==0:
                stack.append(item)
        while stack:
            temp=stack.pop(0)
            ans.append(temp)
            for item in memo[temp]:
                indeg[item]-=1
                if indeg[item]==0:
                    stack.append(item)
        return ans if len(ans)==numCourses else []
a=Solution()
print(a.findOrder(n,pre))