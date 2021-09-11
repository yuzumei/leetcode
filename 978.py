arr=[8,8,9,10,6,8,2,4,2,2,10,6,6,10,10,2,3,5,1,2,10,4,2,0,9,4,9,3,0,6,3,2,3,10,10,6,4,6,4,4,2,5,1,4,1,1,9,8,9,5,3,5,5,4,5,5,6,5,3,3,7,2,0,10,9,7,7,3,5,1,0,9,6,3,1,3,4,4,3,6,3,2,1,4,10,2,3,4,4,3,6,7,6,2,1,7,0,6,8,10]
n=len(arr)
left=0
right=1
choice=0 if arr[0]>arr[1] else 1
'''choice=0 表示a[0]>a[1] a[1]<a[2]……'''
'''choice=1 表示a[0]<a[1] a[1]>a[2]……'''
ans=1
cnt=1
while right<n:
    if arr[left]==arr[right]:
        cnt=1
    else:
        if choice==0:
            if left%2==0:
                if arr[left]>arr[right]:
                    cnt+=1
                    ans = max(cnt, ans)
                else:
                    cnt=1
                    choice=1
            else:
                if arr[left]<arr[right]:
                    cnt+=1
                    ans = max(cnt, ans)
                else:
                    cnt=1
                    choice=1
        if choice==1:
            if left%2==0:
                if arr[left]<arr[right]:
                    cnt+=1
                    ans = max(cnt, ans)
                else:
                    cnt=2
                    choice=0
            else:
                if arr[left]>arr[right]:
                    cnt+=1
                    ans = max(cnt, ans)
                else:
                    cnt=2
                    choice=0
    left+=1
    right+=1
print(ans)