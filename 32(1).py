s = "()(()"
'''dp[i]表示0到i位的最大合法长度'''
# dp=[0]*len(s)
# ans=0
# for i in range(1,len(s)):
#     if s[i]==")":
#         if s[i-1]=="(":
#             dp[i]=(dp[i-2] if i>=2 else 0)+2
#         else:
#             if i-dp[i-1]-1>=0:
#                 if s[i-dp[i-1]-1]=="(":
#                     if i-dp[i-1]-2>=0:
#                         dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
#                     else:
#                         dp[i]=dp[i-1]+2
#     ans=max(dp[i],ans)
# print(max(dp))

'''栈'''
if not s:
    print(0)
s="()(()()(()))(()"
stack = []
ans = 0
for i in range(len(s)):
    # 入栈条件
    if not stack or s[i] == '(' or s[stack[-1]] == ')':
        stack.append(i)     # 下标入栈
    else:
        # 计算结果
        stack.pop()
        ans = max(ans, i - (stack[-1] if stack else -1))
    print(stack,ans)
print(ans)

