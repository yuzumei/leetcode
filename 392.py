class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m=len(s)
        n=len(t)
        i,j=0,0
        while j<n:
            if i==m:
                return True
            if t[j]==s[i]:
                i+=1
            j+=1
        return False