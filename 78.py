nums = [1,2,3]
ans=[]
def combine(a,b):
    ans.append(b)
    if not a:
        return
    for i in range(len(a)):
        temp=a[i+1:]
        tempb=b+[a[i]]
        combine(temp,tempb)
combine(nums,[])
print(ans)

'''二进制'''
