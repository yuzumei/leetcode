def find():
    from collections import defaultdict
    s = "ABBB"
    k = 1
    n=len(s)
    if n<2:
        return n
    s+="0"
    left=0
    right=1
    memo=defaultdict(int)
    for item in s[:2]:
        memo[item]+=1
    while right<n:
        maxstr=max(memo.values())
        if right+1-left-maxstr>k:
            memo[s[left]]-=1
            left+=1
        right+=1
        memo[s[right]]+=1
        print(memo)
    return right-left
print(find())