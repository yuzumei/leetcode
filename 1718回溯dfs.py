n=3
res=[0]*(2*n-1)
remain=list(range(n,0,-1))
'''memo作为保存上一次的记忆'''
def dfs(cnt):
    global res
    global remain
    if 0 not in res:
        return True
    for i in range(len(remain)):
        curnum=remain[i]
        memores=res[:]
        if curnum==1:
            res[cnt]=1
        else:
            if cnt+curnum>=2*n-1 or res[cnt+curnum]!=0:
                continue
            res[cnt]=curnum
            res[cnt+curnum]=curnum
        memoremain=remain[:]
        remain.remove(curnum)
        memocnt=cnt
        while cnt < len(res) and res[cnt] != 0:
            cnt += 1
        if dfs(cnt):#回溯入口
            return True
        cnt=memocnt
        remain=memoremain
        res=memores
    return False
dfs(0)
print(res)