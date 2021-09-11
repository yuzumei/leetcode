s="01"
memo={0:[0,0],1:[0,0]}
for i in range(len(s)):
    if s[i]=="0":
        memo[i%2][0]+=1
    else:
        memo[i%2][1]+=1
ans=max(memo[0][0]+memo[1][1],memo[0][1]+memo[1][0])
print(len(s)-ans)
