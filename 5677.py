s = "zzzzza"
temp=s[0]
cnt=1
ans=0
for i in range(1,len(s)):
    if s[i]==temp:
        cnt+=1
    else:
        ans+=(cnt)*(cnt+1)/2
        cnt=1
        temp=s[i]
ans+=(cnt)*(cnt+1)/2
print(int(ans)%(10**9+7))