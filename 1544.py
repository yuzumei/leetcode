s = "abBAcC"
stack=[]
for item in s:
    if len(stack)==0:
        stack.append(item)
    else:
        if abs(ord(item)-ord(stack[-1]))==32:
            stack.pop()
        else:
            stack.append(item)
ans=""
for item in stack:
    ans+=item
print(ans)