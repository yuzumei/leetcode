def find():
    tokens = [100,200,300,400]
    P = 200
    if len(tokens)==0:
        return 0
    ans=0
    n=len(tokens)
    sortedtokens=sorted(tokens)
    print(sortedtokens)
    if P<sortedtokens[0]:
        return 0
    sumenergy={i:sum(sortedtokens[:i+1]) for i in range(n)}
    left=0
    right=n-1
    while right>=left:
        if P>=sortedtokens[left]:
            P-=sortedtokens[left]
            ans+=1
            left+=1
        else:
            P+=sortedtokens[right]
            ans-=1
            right-=1
        print(ans,left,right)
    return ans
print(find())
