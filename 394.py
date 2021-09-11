s = "2[a3[b]c]3[cd]ef"
stack=[]
multi,res=0,""
for item in s:
    if item.isdigit():
        multi=10*multi+int(item)
    elif item=="[":
        stack.append([multi,res])
        res=""
        multi=0
    elif item=="]":
        temp=stack.pop()
        res=temp[1]+temp[0]*res
    else:
        res=res+item
    print(stack,res)
print(res)
