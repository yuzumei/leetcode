class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        memo=[0]
        while len(memo)<=20:
            memo.append(memo[-1]*5+1)
        while K>6:
            print(K)
            if K%memo[-1]==0 and K//memo[-1]==5:
                return 0
            if K>memo[-1]:
                K-=memo[-1]
            else:
                memo.pop()
        return 0 if K==5 else 5

x=Solution()
print(x.preimageSizeFZF(67348277))