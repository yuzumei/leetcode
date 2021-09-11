'''差分数组'''
'''第一个受影响的差分数组中的元素为f[L],即令f[L]+=x，那么后面数列元素在计算过程中都会加上x；最后一个受影响的差分数组中的元素为f[R],所以令f[R+1]-=x'''
nums = [1,2,3,4,5,6]
requests=[[0,1]]
numsnums=[0]*(len(nums)+1)
for l,r in requests:
    numsnums[l]+=1
    numsnums[r+1]-=1
for i in range(1,len(nums)+1):
    numsnums[i]=numsnums[i]+numsnums[i-1]
a=sorted(nums,reverse=True)
b=sorted(numsnums,reverse=True)
print(sum(a[i]*b[i] for i in range(len(a)-1)))
# numsorder=sorted(nums,reverse=True)
# numsnums={}
# for request in requests:
#     for i in range(request[0],request[1]+1):
#         if i not in numsnums:
#             numsnums[i]=1
#         else:
#             numsnums[i]+=1
# order=sorted(list(numsnums.values()),reverse=True)
# valueorder=order+[0]*(len(nums))
# print(valueorder)
# print(sum(valueorder[i]*numsorder[i] for i in range(len(nums))))