ans=0
def backtrack(row,n,leftexist,rightlist,collist):
    print(collist,leftexist,rightlist)
    global ans
    if row==n:
        ans+=1
        return
    else:
        for i in range(n):
            if i not in collist and row-i not in leftexist and row+i not in rightlist:
                tempcol=collist+[i]
                templeft=leftexist+[row-i]
                tempright=rightlist+[row+i]
                backtrack(row+1,n,templeft,tempright,tempcol)
        return
backtrack(0,12,[],[],[])
print(ans)
