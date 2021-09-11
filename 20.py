s="([)]"
num1=0
num2=0
num3=0
for item in s:
    if num1<0 or num2<0 or num3<0:
        return False
    if item=='(':
        num1+=1
    elif item==')':
        num1-=1
    elif item =='[':
        num2 += 1
    elif item==']':
        num2-=1
    elif item =='{':
        num3+= 1
    elif item=='}':
        num3-=1
if num1==0 and num2==0 and num3==0:
    return True
return False