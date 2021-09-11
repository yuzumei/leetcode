A = [48,99,37,4,-31]
K = 140
def binary(temp,target):
    left=0
    right=len(temp)
    while left<right:
        mid=(left+right)//2
        if temp[mid]>target:
            right=mid
        else:
            left=mid+1
    return left

sums=0
stack=[[-1,0]]
result=len(A)+1
for i,num in enumerate(A):
    sums+=num
    while len(stack)>0 and stack[-1][1]>=sums:
        stack.pop()
    tempans=binary(stack,sums-K)
    if tempans>0:
        result=min(result,i-stack[tempans-1][0])
    stack.append([i,sums])

    return result if result == len(A)+1 else -1