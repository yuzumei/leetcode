nums = [2,5,4,1,3,0,41,0,-5,3,1,0,2,1,5,0,3,1,5,3,0,9,6,-7,0,3,6]
k = 3
stack=[]
for i,num in enumerate(nums[:k]):
    while stack and num>stack[-1][1]:
        stack.pop()
    stack.append([i,num])
ans=[]
point=k
while point<len(nums):
    ans.append(stack[0][1])
    if point-k==stack[0][0]:
        stack.pop(0)
    while stack and nums[point]>stack[-1][1]:
        stack.pop()
    stack.append([point,nums[point]])
    point+=1
ans.append(stack[0][1])
print(ans)
