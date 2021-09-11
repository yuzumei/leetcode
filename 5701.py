class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n=len(s1)
        flag=0
        idx=0
        memo=[]
        while idx<n:
            if s1[idx]!=s2[idx]:
                if flag==1:
                    return False
                if memo==[]:
                    memo=[s1[idx],s2[idx]]
                else:
                    if [s2[idx],s1[idx]]!=memo:
                        return False
                    else:
                        memo=[]
                        flag=1
            idx+=1
        return True if memo==[] else False
x=Solution()
s1 = "banan"
s2 = "kanan"
print(x.areAlmostEqual(s1,s2))
