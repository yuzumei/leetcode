intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
memo=[0]*10000
memo1=[]
ans=[]
maxnum=0
for item in intervals:
    maxnum=max(maxnum,item[1])
    memo[item[0]:item[1]]=[-1]*(item[1]-item[0])
    if item[0]==item[1]:
        memo1.append(item[0])
for num in memo1:
    if memo[num]==0 and memo[num-1]==0:
        ans.append([num,num])
temp=[-1,-1]
for i in range(min(maxnum+2,10000)):
    if memo[i]==-1:
        if temp[0]==-1:
            temp[0]=i
            temp[1]=i
        else:
            temp[1]=i
    else:
        if temp!=[-1,-1]:
            temp[1]+=1
            ans.append(temp)
        temp=[-1,-1]
print(ans)

