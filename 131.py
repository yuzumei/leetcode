import time
time_start=time.time()
s="fffffffffffffff"
def pal(x):
    for word in x:
        if word!=word[::-1]:
            return 0
    return 1
x=list(s)
begin=[]
begin.append(x)
ans=[x]
def dfs(old):
    temp=[]
    for item in old:
        if len(item)>1:
            for i in range(len(item)-1):
                newitem=item[:i]
                newitem.append((item[i]+item[i+1]))
                newitem=newitem+item[i+2:]
                if pal(newitem)==1:
                    if newitem not in ans:
                        ans.append(newitem)
                if newitem not in temp:
                    temp.append(newitem)
        else:
            return 0
    dfs(temp)
dfs(begin)
print(ans)
# res=[]
# def helper(s,temp):
#     if len(s)==0:
#         res.append(temp)
#     else:
#         for i in range(1,len(s)+1):
#             if s[:i]==s[:i][::-1]:
#                 helper(s[i:],temp+[[s[:i]]])
# helper(s,[])
# print(res)

time_end=time.time()
print('totally cost',time_end-time_start)