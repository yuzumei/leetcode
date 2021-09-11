A = [1,2,5]
B = [2,4]
sumA=sum(A)
sumB=sum(B)
for item in A:
    if item+(sumB-sumA)/2 in B:
        print([item,int(item+(sumB-sumA)/2)])