num='199100199'
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num)<3:
            return False
        def check(a,b,num):
            if len(num)==0:
                return True
            if a[0]=="0" and len(a)>=2:
                return False
            if b[0]=="0" and len(b)>=2:
                return False
            temp=str(int(a)+int(b))
            if temp==num[:len(temp)]:
                return check(b,temp,num[len(temp):])
            else:
                return False
        def find():
            for i in range(1,len(num)):
                for j in range(i+1,len(num)):
                    if check(num[:i],num[i:j],num[j:]):
                        return True
                    else:
                        continue
            return False
        return find()