def find():
    A = [0,0,0,1,0,1,1,0]
    K=3
    n=len(A)
    d=[0]*(n+1)
    cnt = 0
    if A[0]==0:
        d[0]+=1
        d[K]-=1
        cnt+=1
    points=1
    while points<=n-K:
        d[points]+=d[points-1]
        A[points]+=d[points]
        if A[points]%2==1:
            points+=1
        else:
            cnt+=1
            d[points]+=1
            d[points+K]-=1
            points+=1
    for item in range(points,len(A)):
        d[item] += d[item - 1]
        A[item] += d[item]
        if A[item]%2==0:
            return -1
    return cnt
print(find())