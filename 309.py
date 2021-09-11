prices=[1,2,3,0,2,5,1,2,0,6,1,1]
f=[-float('inf')]*len(prices) #当天有股票
g=[-float('inf')]*len(prices) #当天没股票
fu=[0]*len(prices) #买股票的那一天
f[0]=-prices[0]
g[0]=0
for i in range(1,len(prices)):
    if fu[i-1]==0:
        f[i]=max(f[i-1],g[i-1]-prices[i])
    else:
        f[i] = max(f[i-1], g[i-2]-prices[i])
    if g[i-1]<f[i-1]+prices[i]:
        fu[i]=1
    g[i]=max(g[i-1],f[i-1]+prices[i])
print(f,g,fu)