height=[1,8,6,2,5,4,8,3,7]
ans=0
left=0
right=len(height)-1
while left<right:
    ans=max(ans,(right-left)*min(height[left],height[right]))
    if height[left]<height[right]:
        left+=1
    else:
        right-=1
print(ans)
