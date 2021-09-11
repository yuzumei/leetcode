s = "11011"
def countans(s):
    if s=="1":
        return 0
    if s[-1]=="0":
        return 1+countans(s[:len(s)-1])
    else:
        for i in range(len(s)-1,0,-1):
            if s[i]=="0":
                return len(s)-i+countans(s[:i]+"1")
        return len(s)+1
print(countans(s))
