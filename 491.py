class Solution:
    def findSubsequences(self, nums):
        import collections
        memo=collections.defaultdict(set)
        ans=collections.defaultdict(list)
        for num in nums:
            for i in memo:
                if num>=i:
                    temp = [] if num in memo[i] else  [[i,num]]
                    if num not in memo[i]:
                        for item in ans[i]:
                            if num>=item[-1]:
                                temp.append(item+[num])
                    else:
                        for item in ans[i]:
                            if num>=item[-1] and item+[num] not in ans[i]:
                                temp.append(item+[num])
                    memo[i].add(num)
                    ans[i]+=temp
            if num not in ans:
                ans[num] = []
                memo[num] = set()
        res=[]
        for i in ans:
            res+=ans[i]
        return res

x=Solution()
print(x.findSubsequences([3,9,3,9,4,6,6,5,5]))