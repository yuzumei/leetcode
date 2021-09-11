s = "dvdf"
ans=0
memo=dict()
queue=[]
for item in s:
    print(queue,memo)
    if item in memo:
        ans=max(ans,len(queue))
        while queue[0]!=item:
            del memo[queue.pop(0)]
        queue.pop(0)
    memo[item]=0
    queue.append(item)
print(max(ans,len(queue)))
