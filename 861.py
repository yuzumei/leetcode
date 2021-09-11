A=[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
n=len(A)
m=len(A[0])
for i in range(n):
    if A[i][0]!=1:
        for j in range(m):
            A[i][j]=(A[i][j]+1)%2
ans=[n]
for i in range(1,m):
    temp=0
    for j in range(n):
        if A[j][i]==1:
            temp+=1
    ans.append(max(temp,n-temp))
num=0
for i,item in enumerate(ans):
    num+=item*(2**(m-1-i))
print(num)