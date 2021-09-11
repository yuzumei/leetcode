class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math
        l,r=0,int(math.sqrt(c))
        while l<=r:
            if c==l*l+r*r:
                return True
            elif c<l*l+r*r:
                r-=1
            else:
                l+=1
        return False
x=Solution()
print(x.judgeSquareSum(36))