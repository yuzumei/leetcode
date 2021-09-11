nums = [431,922,158,60,192,14,788,146,788,775,772,792,68,143,376,375,877,516,595,82,56,704,160,403,713,504,67,332,26]
maxOperations =80
def check(num):
    ans=0
    for s in nums:
        if s>num:
            if s%num==0:
                ans+=(s//num)-1
            else:
                ans+=(s//num)
    return ans>maxOperations
left,right=1,max(nums)
mid=(left+right)//2
ans=right
while abs(left-right)>1:
    print(ans)
    if check(mid):
        left=mid
    else:
        ans=min(ans,mid)
        right=mid
    mid = (left + right) // 2
print(ans)
