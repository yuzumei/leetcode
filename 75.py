nums = [0,2,0,1,2,1,0,1,0]
n=len(nums)
cnt2=0
cnt1=0
for _ in range(n):
    temp=nums.pop(0)
    if temp==2:
        nums.append(2)
        cnt2+=1
    elif temp==1:
        nums.insert(n-1-cnt2,1)
        cnt1+=1
    else:
        nums.insert(n-1-cnt2-cnt1,0)
print(nums)