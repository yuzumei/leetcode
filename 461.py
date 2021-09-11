x,y=1,4
n=x^y
cnt=0
while n>0:
    if n&1:
        cnt+=1
    n=n>>1
print(cnt)