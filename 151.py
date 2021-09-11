s = "blue is sky the"
n=len(s)
left=0
right=0
ans=""
while right<=n-1:
    if s[right]==" ":
        if left==right:
            left+=1
            right+=1
        else:
            word=s[left:right]
            ans=" "+word+ans
            left=right
    else:
        if right==n-1:
            ans=' '+s[left:right+1]+ans
        right=right+1
print(ans[1:])