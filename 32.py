s = "()((((())))))((())(()))(())(((())((())()()"
left=0
temp=[0]
tempmax=0
for item in s:
    if item=="(":
        left+=1
    else:
        left-=1
    if left<0:
        left=0
    tempmax=max(left,tempmax)
    temp.append(left)
temp.append(-1)
record=0
print(temp)
for i in range(1,tempmax):
    leftpoint=0
    rightpoint=0
    for j in range(len(temp)):
        if temp[j]==i:
            if leftpoint==0:
                leftpoint=j
            else:
                rightpoint=j
            record=max(rightpoint-leftpoint,record)
        if temp[j]<i:
            leftpoint=0
            rightpoint=0
print(record)