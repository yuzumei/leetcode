heights=[6,7,5,2,4,5,9,3]
def search(heights):
    leftstack=[]
    leftnum=[]
    for i,num in enumerate(heights):
        if not leftstack:
            leftstack.append([num,i])
            leftnum.append(-1)
        else:
            while leftstack:
                if num<=leftstack[-1][0]:
                    leftstack.pop()
                else:
                    break
            if leftstack:
                leftnum.append(leftstack[-1][1])
            else:
                leftnum.append(-1)
            leftstack.append([num,i])
    return leftnum
leftnum=search(heights)
rightnum=search(heights[::-1])[::-1]
print(leftnum,rightnum)
ans=-1
for i in range(len(heights)):
    ans=max(ans,(len(heights)-2-rightnum[i]-leftnum[i])*heights[i])
print(ans)
'''遍历两次'''
def twoside(heights):
    n=len(heights)
    if n==0:
        return 0
    leftnum=[0]*n
    rightnum=[n]*n
    stack=[]
    for i,num in enumerate(heights):
        while stack and num<=stack[-1][1]:
            temp=stack.pop()
            rightnum[temp[0]]=i
        leftnum[i]=stack[-1][0] if stack else -1
        stack.append([i,num])
    ans=max((rightnum[i]-leftnum[i]-1)*heights[i] for i in range(n))
    return ans
print(twoside(heights))
