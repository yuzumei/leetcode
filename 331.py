def x():
    preorder="9,#,#,1"
    wait=preorder.split(",")
    target=1
    for item in wait:
        target-=1
        if target<0:
            return False
        if item!="#":
            target+=2
    return True if target==0 else False
print(x())