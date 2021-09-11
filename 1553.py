class Solution:
    def minDays(self, n: int) -> int:
        if n<=1:
            return n
        return 1+min(self.minDays(n//2)+n%2,n%3+self.minDays(n//3))
x=Solution()
print(x.minDays(2000000000))

# cnt = 0
# while n > 1:
#     if n % 3 == 0:
#         n = n // 3
#     elif n % 3 == 2:
#         n -= 1
#     else:
#
#     cnt += 1