cardPoints = [1,79,80,1,1,1,200,1]
k = 3
n=len(cardPoints)
ans=sum(cardPoints[:k])
tempmax=ans
for i in range(k):
    tempmax=tempmax-cardPoints[k-i-1]+cardPoints[n-1-i]
    ans=max(tempmax,ans)
print(ans)
