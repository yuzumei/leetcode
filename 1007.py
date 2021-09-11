A = [1,2,1,1,1,2,2,2]
B = [2,1,2,2,2,2,2,2]
C=list(zip(A,B))
flag=0
a=A[0]
ansA=[1,0]
b=B[0]
ansB=[0,1]
for i in range(1,len(A)):
    if a not in C[i]:
        flag+=1
        ansA=[99999,99999]
        break
    if C[i][0]==a and C[i][1]==a:
        continue
    if C[i][0]==a:
        ansA[0]+=1
    else:
        ansA[1]+=1
for i in range(1,len(A)):
    if b not in C[i]:
        flag+=1
        ansB = [99999, 99999]
        break
    if C[i][0]==b and C[i][1]==b:
        continue
    if C[i][0]==b:
        ansB[0]+=1
    else:
        ansB[1]+=1
if flag==2:
    print("-1")
else:
    print(min(min(ansA),min(ansB)))