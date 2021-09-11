class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == '-':
            for i in range(1,len(n)):
                if int(n[i]) > x:
                    return n[:i]+'%s'%x+n[i:]
            return n+'%s'%x
        else:
            for i in range(len(n)):
                if int(n[i]) < x:
                    return n[:i]+'%s'%x+n[i:]
            return n + '%s' % x

x=Solution()
print(x.maxValue('-684135467643',5))