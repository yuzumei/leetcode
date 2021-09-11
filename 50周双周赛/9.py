class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n<k:
            return n
        cnt=0
        while n>=k**(cnt+1):
            cnt+=1
        return n//(k**cnt)+self.sumBase(n%(k**cnt),k)
x=Solution()
print(x.sumBase(n = 99, k = 10))