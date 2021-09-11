def x():
    A = [1,1,1,0,0,0,1,1,1,1,0]
    K = 2
    n=len(A)
    A.insert(0,0)
    A.append(0)
    ans=0
    memo=[0]
    for i in range(1,n+2):
        if A[i]==0:
            memo.append(i)
        if len(memo)==K+2:
            ans=max(ans,memo[-1]-memo.pop(0)-1)
    return max(ans,memo[-1]-memo.pop(0)-1)

print(x())