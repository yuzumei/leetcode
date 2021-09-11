a = "101011"
b = "1011"
c=int(a)+int(b)
s=([0]+list(str(c)))[::-1]
t=0
while t<=len(s)-2:
    if s[t]=="2" or s[t]=="3":
        s[t]=str(int(s[t])-2)
        s[t+1]=str(int(s[t+1])+1)
    t+=1
ans=" "
for item in s[::-1]:
    ans+=str(item)
print(int(ans))