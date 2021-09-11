bits = [1, 1, 1, 0]
if bits[-1]==0:
    return False
points=0
while points<len(bits)-1:
    if bits[points]==1:
        points+=2
    else:
        points+=1
return points==len(bits)-1