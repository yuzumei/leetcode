height =[1]
ans=0
left=0
i=height.index(max(height))
for num in height[:i+1]:
    if num>left:
        left=num
    else:
        ans+=(left-num)
left=0
for num in height[i:][::-1]:
    if num>left:
        left=num
    else:
        ans+=(left-num)
print(ans)