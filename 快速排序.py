def quicksort(temp):
    if len(temp)<2:
        return temp
    left=[]
    right=[]
    x=temp[0]
    temp.remove(x)
    for item in temp:
        if item>x:
            right.append(item)
        else:
            left.append(item)
    return quicksort(left)+[x]+quicksort(right)
x=[5,6,8,1,4,6,9,7,4,2,6,7,10,3,5,4,9]
print(quicksort(x))
