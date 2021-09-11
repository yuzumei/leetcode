class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if K<=2:
            return 0 if K==1 else 1
        if N % 2 == 0:
            return 1-self.kthGrammar(N-1,2**(N-1)+1-K) if K>2**(N-2) else self.kthGrammar(N-1,K)
        else:
            return self.kthGrammar(N-1,min(2**(N-1)+1-K,K))

x=Solution()
print(x.kthGrammar(5,9))