boxes = "101101"
n=len(boxes)
ans=[0]*n
sumpoint=0
cnt=0
for i in range(n):
    if boxes[i]=="1":
        cnt+=1
        sumpoint+=i
flag=0 if boxes[0]=='0' else 1
ans[0]=sumpoint
for i in range(1,n):
    ans[i]=ans[i-1]-cnt+2*flag
    if boxes[i]=="1":
        flag+=1
print(ans)