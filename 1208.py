s = "abcd"
t = "cdef"
cost = 3
n=len(s)
wordcost=[0]*n
for i in range(n):
    wordcost[i]=abs(ord(s[i])-ord(t[i]))
left=0
right=1
ans=0
sumcost=wordcost[0]
while right<=n:
    if sumcost<=cost:
        ans = max(ans, right - left)
        if right!=n:
            sumcost+=wordcost[right]
        right+=1
    else:
        sumcost-=wordcost[left]
        left+=1
print(ans)