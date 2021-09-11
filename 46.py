nums=[1,2,3]
ans=[]
def combine(a,b):
    if not a:
        ans.append(b)
        return
    for item in a:
        temp=a[:]
        temp.remove(item)
        tempb=b+[item]
        combine(temp,tempb)
combine(nums,[])
print(ans)