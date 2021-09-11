class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s+=' '
        ans=''
        temp=''
        i=0
        while k>0:
            if s[i]==' ':
                temp+=' '
                ans+=temp
                temp=''
                k-=1
            else:
                temp+=s[i]
            i+=1
        return ans[:-1]

x=Solution()
print(x.truncateSentence(s = "What is the solution to this problem", k = 4))