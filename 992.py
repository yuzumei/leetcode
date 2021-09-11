A = [27,27,43,28,11,20,1,4,49,18,37,31,31,7,3,31,50,6,50,46,4,13,31,49,15,52,25,31,35,4,11,50,40,1,49,14,46,16,11,16,39,26,13,4,37,39,46,27,49,39,49,50,37,9,30,45,51,47,18,49,24,24,46,47,18,46,52,47,50,4,39,22,50,40,3,52,24,50,38,30,14,12,1,5,52,44,3,49,45,37,40,35,50,50,23,32,1,2]
K = 20
left=0
right=K
# from collections import defaultdict
# ans=defaultdict(list)
# memo=defaultdict(set)
# def subarray(left,right):
#     if left + right not in ans[left - right]:
#         ans[left - right].append(left + right)
#     else:
#         return 0
#     if right>len(A):
#         return 0
#     if len(set(A[left:right])) < K:
#         return subarray(left,right+1)
#     elif len(set(A[left:right])) == K:
#         memo[left-right].add(left+right)
#         return 1+subarray(left+1,right)+subarray(left,1+right)
#     else:
#         return subarray(left+1,right)
# subarray(0,K)
# res=0
# for item in memo:
#     res+=len(memo[item])
# print(res)
'''超时'''
from collections import defaultdict
ans=defaultdict(int)
memo=defaultdict(int)
for item in A[left:right]:
    ans[item]+=1
cnt=0
while right<=len(A):
    if len(ans)>K:
        if ans[A[left]]==1:
            del ans[A[left]]
        else:
            ans[A[left]]-=1
        left += 1
    elif len(ans)==K:
        cnt+=1
        temp=defaultdict(int)
        for item in A[left:right]:
            temp[item]+=1
            if temp[item]<ans[item]:
                cnt+=1
            else:
                break
        if right!=len(A):
            ans[A[right]]+=1
        right += 1
    else:
        if right!=len(A):
            ans[A[right]]+=1
        right += 1

print(cnt)
