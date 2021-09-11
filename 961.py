A=[5,1,5,2,5,3,5,4]
referdict={}
for i in range(len(A)):
    # referdict[A[i]]=i
    if referdict[A[i]]!=i:
        return A[i]