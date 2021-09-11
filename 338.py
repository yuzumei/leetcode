num=5
ans=[0]*(num+1)
temp=0
for i in range(1,len(ans)):
    if i==2**temp:
        ans[i]=1
        temp+=1
    else:
        ans[i]=ans[i-2**(temp-1)]+1
print(ans)