def x():
    A=[6,5,4,4]
    flag=0
    for i in range(len(A)-1):
        if A[i]==A[i+1]:
            pass
        elif A[i]>A[i+1]:
            if flag==0:
                flag=1
            elif flag==-1:
                return False
        else:
            if flag == 0:
                flag = -1
            elif flag == 1:
                return False
    return True
print(x())