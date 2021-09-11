T = [73, 74, 75, 71, 69, 72, 76, 73]
ans=[0]*len(T)
stack=[]
for i in range(len(T)):
    if not stack:
        stack.append(i)
    else:
        while stack and T[i]>T[stack[-1]]:
            indexnum=stack.pop()
            ans[indexnum]=i-indexnum
        stack.append(i)
print(ans)