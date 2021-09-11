price=[2,5]
special=[[3,0,5],[0,2,8],[3,2,12]]
needs=[3,2]
def dfs(needs):
    print(needs)
    res=sum([price[i]*needs[i] for i in range(len(needs))])
    for s in special:
        newneeds=[needs[i]-s[i] for i in range(len(needs))]
        print(newneeds)
        if min(newneeds)>=0:
            res=min(res,dfs(newneeds)+s[-1])
    print(res)
    return res
dfs(needs)