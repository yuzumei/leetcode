dominoes = [[1,2],[2,1],[3,4],[5,6]]
count={}
for item in dominoes:
    a=min(item[0],item[1])
    b = max(item[0], item[1])
    if 10*a+b not in count:
        count[10 * a + b] = 1
    else:
        count[10*a+b]+=1
allnum=list(count.values())
ans=0
for item in allnum:
    if item>1:
        ans+=(item*(item-1)/2)
print(int(ans))
