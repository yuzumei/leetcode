class Solution:
    def smallestGoodBase(self, n: str) -> str:
        import math
        cnt=int(math.log2(n))
        for i in range(cnt,0,-1):  #i是多少位
            left=2
            right=int(pow(n,1/i))+1
            while left<=right:
                num = (left + right) // 2  # num是几进制
                s=sum(pow(num,j) for j in range(i+1))
                if s==n:
                    return num
                elif s>n:
                    right=num-1
                elif s<n:
                    left=num+1
        return n-1

x=Solution()
print(x.smallestGoodBase(727004545306745403))