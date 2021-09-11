asteroids = [-5, 10, -5,32,2,-5,-8,2,1,6,-9,4,6,-7,1,3,-6]
stack=[]
ans=[]
for item in asteroids:
    if len(stack)==0 and item<0:
        ans.append(item)
        continue
    if item>0:
        stack.append(item)
        print(stack)
        continue
    if len(stack)>0 and item<0:
        while len(stack)>0:
            if stack[-1]==abs(item):
                stack.pop()
                break
            elif stack[-1]<abs(item):
                stack.pop()
                if len(stack)==0:
                    ans.append(item)
            else:
                break
ans+=stack
print(ans)

