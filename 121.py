prices=[1,2,5,8,4,1,3,5,13,1,5,43,1,4,31,4,6,3,64,6,48,0,31,5,8]
ans=0
big,small=prices[0],prices[0]
for i in range(1,len(prices)):
    if prices[i]<small:
        ans=max(ans,big-small)
        big, small = prices[i], prices[i]
    if prices[i]>big:
        big=prices[i]
print(max(ans,big-small))