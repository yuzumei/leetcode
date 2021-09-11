s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
class Solution:
    def lastSubstring(self, s: str) -> str:
        memo=''
        n=len(s)
        for i in range(n-1,-1,-1):
            flag=1
            temp=s[i:]
            m=len(memo)
            for j in range(m):
                if ord(temp[j])>ord(memo[j]):
                    flag=1
                    break
                elif ord(temp[j])<ord(memo[j]):
                    flag=0
                    break
            memo=temp if flag==1 else memo
        return memo

x=Solution()
print(x.lastSubstring(s))