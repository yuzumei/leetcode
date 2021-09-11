class Solution:
    def getOrder(self, tasks):
        import time as TT
        x=TT.time()
        n=len(tasks)
        import collections
        memo=collections.defaultdict(list)
        time=set()
        for i,task in enumerate(tasks):
            memo[task[0]].append([task[1],i])
            time.add(task[0])
        queue=sorted(list(time))
        start=queue[0]
        ans=[]
        res=[]
        print(TT.time()-x)
        import heapq
        heapq.heapify(res)
        while len(ans)!=n:
            cnt=0
            for num in queue:
                if num<=start:
                    cnt+=1
                    for item in memo[num]:
                        heapq.heappush(res,item)
                else:
                    break
            if queue:
                queue=queue[cnt:]
            else:
                while res:
                    temp = heapq.heappop(res)
                    ans.append(temp[1])
                break
            if res:
                temp=heapq.heappop(res)
                ans.append(temp[1])
                start+=temp[0]
            else:
                start=queue[0]
        # import heapq
        # wait = []
        # taskID = sorted(range(len(tasks)), key=lambda x:-tasks[x][0])
        # time = 0
        # res = []
        # while wait or taskID:
        #     while taskID and tasks[taskID[-1]][0] <= time:
        #         i = taskID.pop()
        #         heapq.heappush(wait, [tasks[i][1], i])
        #     if not wait:
        #         time = tasks[taskID[-1]][0]
        #         continue
        #     t, i = heapq.heappop(wait)
        #     res.append(i)
        #     time += t
        y=TT.time()
        print(y-x)
        return ans

x=Solution()
s=[]
for i in range(1,100000):
    s.append([i,1])
print(x.getOrder(tasks = s))
