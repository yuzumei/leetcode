s1= "ab"
s2 = "eidbaooo"
def checkInclusion(s1, s2):
    if len(s1)>len(s2):
        return False
    ans=0
    m=len(s1)
    n=len(s2)
    for item in s1:
        ans+=ord(item)*ord(item)
    test=0
    for item in s2[:m]:
        test+=ord(item)*ord(item)
    left=0
    right=m
    while right<n:
        if test==ans:
            return True
        else:
            test-=ord(s2[left])*ord(s2[left])
            test += ord(s2[right]) * ord(s2[right])
        left+=1
        right+=1
        print(ans,test)
    if test==ans:
        return True
    return False
print(checkInclusion(s1,s2))