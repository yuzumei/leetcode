names = ["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]
from collections import defaultdict
ansdict=defaultdict(int)
res=[]
for item in names:
    count = ansdict[item]
    temp = item
    if count==0:
        ansdict[item]=1
    else:
        while item in ansdict:
            item = temp + "("+ str(count) +")"
            count += 1
        ansdict[item]=1
        ansdict[temp]=count
    res.append(item)
print(res)