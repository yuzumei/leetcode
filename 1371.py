s = "amntyyaw"
vowel=('a','e','i','o','u')
from collections import defaultdict
memo=defaultdict(list)
def twototen(temp):
    return 16*temp[0]+8*temp[1]+4*temp[2]+2*temp[3]+temp[4]
start=[0,0,0,0,0]
for i in range(len(s)):
    if s[i]=="a":
        start[0]=(start[0]+1)%2
    elif s[i]=="e":
        start[1]=(start[1]+1)%2
    elif s[i]=="i":
        start[2]=(start[2]+1)%2
    elif s[i]=="o":
        start[3]=(start[3]+1)%2
    elif s[i] == "u":
        start[4]=(start[4]+1)%2
    memo[twototen(start)].append(i)
print(memo)
ans=0
for item in memo:
    if len(memo[item])>=2:
        if item!=0:
            ans=max(ans,memo[item][-1]-memo[item][0])
        else:
            ans = max(ans, memo[item][-1]+1)
print(ans)
