s = "aaa"
p = "a*a"
def match(s1,p1):
    s=list(s1)
    p=list(p1)
    while len(s)>0 or len(p)>0:
        print(s, p)
        if len(p)==0 and len(s)!=0:
            return False
        if len(s) == 0 and len(p)!=0:
            if len(p)>=2 and p[1]=='*':
                p.pop(0)
                p.pop(0)
            else:
                return False
        if len(p)>=2 and p[0]=='.' and p[1]=='*':
            s=[]
            p.pop(0)
            p.pop(0)
        elif s[0]==p[0]:
            if len(p)>=2 and p[1]=='*':
                temp=s[0]
                while s and s[0]==temp:
                    s.pop(0)
                p.pop(0)
                p.pop(0)
            else:
                s.pop(0)
                p.pop(0)
        else:
            if p[0]==".":
                p[0]=s[0]
            elif len(p) >= 2 and p[1] == '*':
                p.pop(0)
                p.pop(0)
            else:
                return False
    return True
print(match(s,p))

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]

