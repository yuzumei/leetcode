nums = [200,100,14]
threshold = 10
n=len(nums)
target=sorted(nums)
small=1
big=target[-1]
ans=(small+big)//2
minus=big-small
temp=big
count=0
def solve(x):
    temp=0
    for item in nums:
        temp=temp+(item+x-1)//x
    return temp
while 2**count<=minus+1:
    if solve(ans)>threshold:
        small=ans
        if (ans+big)%2==0:
            ans=(ans+big)//2
        else:
            ans=1+(ans+big)//2
    else:
        if temp>ans:
            temp=ans
        big=ans
        ans=(ans+small)//2
    count+=1
    print(temp,small,big)
