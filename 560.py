nums = [1,1,1]
k = 2
memo={0:1}
cnt=0
temp=0
for num in nums:
    temp+=num
    if temp-k in memo:
        cnt+=memo[temp-k]
    if temp in memo:
        memo[temp]+=1
    else:
        memo[temp]=1
print(cnt)
