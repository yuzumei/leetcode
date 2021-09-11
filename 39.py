candidates = [2,3,6,7,4]
target = 7
candidates.sort()
ans=[]
def dfs(candidate,res,target):
    if target<0 or len(candidate)==0:
        return
    elif target==0:
        ans.append(res)
    else:
        for i in range(len(candidate)):
            if candidate[i]>target:
                break
            dfs(candidate[i:],res+[candidate[i]],target-candidate[i])
dfs(candidates,[],target)
print(ans)