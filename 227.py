s="5+2*6 +5-4/5+ 6+4 1+2+9-79*8/6- 4+5"
stack=[]
alphastack=[]
a=''
for alpha in s:
    if alpha==" ":
        pass
    elif alpha in ('+','-','*','/'):
        alphastack.append(alpha)
        stack.append(a)
        a=''
    else:
        a+=alpha
stack.append(a)
point=0
alphapoint=0
while alphapoint<len(alphastack):
    if alphastack[alphapoint]=='*':
        alphastack.pop(alphapoint)
        a=stack.pop(point)
        b=stack.pop(point)
        stack.insert(point,int(a)*int(b))
        alphapoint-=1
        point-=1
    elif alphastack[alphapoint]=='/':
        alphastack.pop(alphapoint)
        a=stack.pop(point)
        b=stack.pop(point)
        stack.insert(point,int(a)//int(b))
        alphapoint -= 1
        point-=1
    point+=1
    alphapoint+=1
while len(stack)!=1:
    a=stack.pop(0)
    b=stack.pop(0)
    c=alphastack.pop(0)
    if c=='+':
        stack.insert(0,int(a)+int(b))
    else:
        stack.insert(0,int(a)-int(b))
print(stack[-1])

