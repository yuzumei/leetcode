def x():
    word1 = "abcjl"
    word2 = "pqt4235"
    n1=len(word1)
    n2=len(word2)
    ans=""
    if n1==n2:
        for i in range(n1):
            ans+=word1[i]
            ans+=word2[i]
    elif n1>n2:
        for i in range(n2):
            ans+=word1[i]
            ans+=word2[i]
        ans+=word1[n2:]
    else:
        for i in range(n1):
            ans += word1[i]
            ans += word2[i]
        ans += word2[n1:]
    return ans
print(x())