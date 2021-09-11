class Solution:
    def makeStringSorted(self, s: str) -> int:
        class Solution:
            def makeStringSorted(self, s: str) -> int:
                mod = 10 ** 9 + 7

                # 快速幂，用来计算 x^y mod m
                def quickmul(x: int, y: int) -> int:
                    # Python 有方便的内置函数
                    return pow(x, y, mod)

                n = len(s)

                # fac[i] 表示 i! mod m
                # facinv[i] 表示 i! 在 mod m 意义下的乘法逆元
                fac, facinv = [0] * (n + 1), [0] * (n + 1)
                fac[0] = facinv[0] = 1
                for i in range(1, n):
                    fac[i] = fac[i - 1] * i % mod
                    # 使用费马小定理 + 快速幂计算乘法逆元
                    facinv[i] = quickmul(fac[i], mod - 2)

                # freq 存储每个字符出现的次数
                freq = collections.Counter(s)

                ans = 0
                for i in range(n - 1):
                    # rank 求出比 s[i] 小的字符数量
                    rank = sum(occ for ch, occ in freq.items() if ch < s[i])
                    # 排列个数的分子
                    cur = rank * fac[n - i - 1] % mod
                    # 依次乘分母每一项阶乘的乘法逆元
                    for ch, occ in freq.items():
                        cur = cur * facinv[occ] % mod

                    ans += cur
                    freq[s[i]] -= 1
                    if freq[s[i]] == 0:
                        freq.pop(s[i])

                return ans % mod

        # n=len(s)
        # dp=[0]*n
        # for i in range(1,n):
        #     dp[i]=dp[i-1]+i*(1+dp[i-1])
        # '''dp[i]表示i+1位倒序重排次数'''
        # ans=0
        # import collections
        # memo=collections.defaultdict(int)
        # memo[ord(s[-1])-ord('a')]=1
        # for i in range(n-2,-1,-1):
        #     num=ord(s[i])-ord('a')
        #     temp=0
        #     for j in range(num):
        #         temp+=memo[j]
        #     ans+=(temp*(1+dp[n-2-i]))
        #     memo[num]=1
        # return ans%(10**9+7)
x=Solution()
print(x.makeStringSorted('aabbaa'))