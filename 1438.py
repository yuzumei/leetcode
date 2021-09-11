nums = [7,40,10,10,40,39,96,21,54,73,33,17,2,72,5,76,28,73,59,22,100,91,80,66,5,49,26,45,13,27,74,87,56,76,25,64,14,86,50,38,65,64,3,42,79,52,37,3,21,26,42,73,18,44,55,28,35,87]
limit = 63
memomin=[nums[0],0]
memomax=[nums[0],0]
left=0
right=1
ans=0
while right<len(nums):
    if nums[right]<memomin[0]:
        memomin=[nums[right],right]
    if nums[right]>memomax[0]:
        memomax=[nums[right],right]
    if memomax[0]-memomin[0]>limit:
        ans=max(right-left,ans)
        if nums[right]==memomin[0]:
            
# memomin=nums[0]
# memomax=nums[0]
# left=0
# right=1
# ans=0
# while right<len(nums):
#     print(left,right,ans,memomax,memomin)
#     memomin=min(memomin,nums[right])
#     memomax=max(memomax,nums[right])
#     ans = max(right - left, ans)
#     if memomax-memomin>limit:
#         if nums[right]==memomax:
#             memomin=float('inf')
#             for i in range(right,left,-1):
#                 if memomax-nums[i]<=limit:
#                     memomin=min(nums[i],memomin)
#                     left=i
#                 else:
#                     break
#         else:
#             memomax=0
#             for i in range(right,left,-1):
#                 if nums[i]-memomin<=limit:
#                     memomax=max(nums[i],memomax)
#                     left=i
#                 else:
#                     break
#     right+=1
# ans = max(right - left, ans)
# print(ans)