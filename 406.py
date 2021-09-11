people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
sortpeople=sorted(people,key=lambda x:x[0],reverse=True)
import collections
indeg=collections.defaultdict(list)
memo=collections.defaultdict(int)
stack=[]
for item in sortpeople:
    memo[item[0]]=0
    if item[1]==0:
        stack.append(item)
    else:
        indeg[item[0]].append(item)
for i in indeg:
    indeg[i].sort()
print(indeg,stack)
ans=[]
while stack:
    temp=stack.pop()
    ans.append(temp)
    for i in memo:
        if i<=temp[0]:
            memo[i]+=1
        while indeg[i] and indeg[i][0][1]<=memo[i]:
            stack.append(indeg[i].pop(0))
print(ans)
