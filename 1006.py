n=4
if n%4==0:
    ans=-5
elif n%4==1:
    ans=-1
elif n%4==2:
    ans=-2
else:
    ans=-6
x=n//4
if x==0:
    return ans
else:
    for i in range(x):
        temp=n-4*i
        if i==0:
            ans+=(temp*(temp-1)//(temp-2)+temp-3)
        else:
            ans-=(temp*(temp-1)//(temp-2)-temp+3)
    return ans
