s = "-(1+(4+5+2)-3)+(6+8)"
class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        stacknum=[]
        stack1=[]
        temp=''
        s='('+s+')'
        for alpha in s:
            if alpha=='(':
                stack.append(alpha)
                if len(stack1)!=0:
                    stack1.append(',')
            elif alpha==')':
                stack.pop()
                if temp!='':
                    stacknum.append(int(temp))
                if stack1 and stack1[-1]!=',':
                    ans=0
                    while stack1 and stack1[-1] != ',':
                        a=stacknum.pop()
                        if stack1.pop()=='+':
                            ans+=a
                        else:
                            ans-=a
                    if len(stacknum)!=0:
                        a=stacknum.pop()
                        ans+=a
                    stacknum.append(ans)
                temp=''
                if stack1 and stack1[-1]==',':
                    stack1.pop()
            elif alpha=='+' or alpha=='-':
                if temp!='':
                    stacknum.append(int(temp))
                temp=''
                stack1.append(alpha)
            elif alpha.isalnum():
                temp+=alpha
        return stacknum[0]

x=Solution()
print(x.calculate(s))
