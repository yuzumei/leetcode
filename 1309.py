s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
ans=""
for i in range(len(s)):
    if s[i]=="#":
        continue
    if s[i]=="0":
        temp=ans[-1]
        ans=ans[:-1]
        if temp=="1":
            ans+="j"
        else:
            ans+="t"
    if s[i]==1:
        ans
