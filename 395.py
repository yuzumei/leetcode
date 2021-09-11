s = "a"
k = 2
import collections
ans=0
def two(s):
    global ans
    memo=collections.defaultdict(list)
    for i,item in enumerate(s):
        memo[item].append(i)
    queue=[-1]
    for item in memo:
        if len(memo[item])<k:
            queue+=memo[item]
    queue.append(len(s))
    if len(queue)==2:
        ans=max(ans,len(s))
        return
    for i in range(1,len(queue)):
        two(s[queue[i-1]+1:queue[i]])
two(s)
print(ans)

