points = [[1,3],[2,0],[5,10],[6,-10]]
k=1
ans=float("-inf")
queue=[]
for point in points:
    x=point[0]
    y=point[1]
    while queue and x-queue[0][0]>k:
        queue.pop(0)
    if queue:
        ans=max(ans,x+y+queue[0][1])
    while queue and queue[-1][1]<=y-x:
        queue.pop()
    queue.append([x,y-x])
    print(queue)