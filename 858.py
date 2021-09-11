p=10
q=3
def find(p,q):
    if p%q==q/2:
        return 0
    k=1
    while (k*p)%q!=0:
        k+=1
    if k%2==0:
        return 0
    else:
         return 2 if ((k*p)/q)%2==0 else 1
print(find(2,1))