arr = [1,2,3,5]
k = 3
n=len(arr)
memo={}
def under(x):
    count=0
    maxfrac=0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]/arr[j]<x:
                count+=1
                maxfrac=max(maxfrac,arr[i]/arr[j])
            else:
                break
    return [count,maxfrac]

left=0
right=1
mid = (left + right) / 2
while right-mid>1e-9:
    mid = (left + right) / 2
    if under(mid)[0]>k:
        left=mid
    else:
        right=mid
print(memo)
