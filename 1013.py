arr=[10,-10,10,-10,10,-10,10,-10]
def find(arr):
    for i in range(1,len(arr)):
        arr[i]=arr[i-1]+arr[i]
    ans=arr[-1]
    if ans%3!=0:
        return False
    else:
        cnt=0
        last=ans/3
        for i in range(len(arr)):
            if arr[i]==last:
                cnt+=1
                last*=2
                if cnt==2 and i!=len(arr)-1:
                    return True
    return False
print(find(arr))