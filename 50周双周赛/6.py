class Solution:
    def getOrder(self, tasks):
        import collections
        n=len(tasks)
        memo=collections.defaultdict(list)
        time=set()
        for i,task in enumerate(tasks):
            memo[task[0]].append([task[1],i])
            time.add(task[0])
        for item in memo:
            memo[item].sort()
        queue=sorted(list(time))
        ans=[]
        temp=[queue.pop(0)]
        while len(ans)!=n:
            res,time=float('inf'),-1
            if temp:
                for x in temp:
                    (res,time)=(memo[x][0][0],x) if memo[x][0]<res else (res,time)
            newtime=x+memo[x][0][0]
            while queue and queue[0]<=newtime:
                temp.append(queue.pop(0))



