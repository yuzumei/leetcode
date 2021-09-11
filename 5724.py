a,b=[32,63,30,87,5,79,98,19,4,24,28,89,81,40,89,46,14,42,54,20,68,94,15,56,52,97,74,37,92,49,41,75,38,34,59,2,49,8,23,8,48,74,99,31,60,96,63,20,71,62,48,77,11,95,9,16,83,7,98,33,67,29,80,88,99,66,66,57,79,44,98,22,42,93,33,72,10,49,83,51,66,71,96,53,33,96,54,64,64,10,8,41,52,98,77,17,77,11,31,11],[84,31,34,15,68,67,16,18,94,34,55,68,56,80,93,71,47,86,96,20,93,68,90,100,37,86,22,37,57,67,48,96,43,77,89,57,5,99,33,70,13,38,31,56,97,11,84,20,4,19,29,11,64,64,52,59,70,33,34,27,33,94,92,11,59,53,74,38,26,82,63,38,48,72,100,28,20,46,49,72,99,71,98,66,44,99,95,12,56,39,72,1,6,53,34,13,9,81,16,22]
class Solution:
    def minAbsoluteSumDiff(self, nums1, nums2) -> int:
        # n=len(nums1)
        # import collections
        # memo=collections.defaultdict(int)
        # record=collections.defaultdict(int)
        # ans = 0
        # for i in range(n):
        #     ans+=abs(nums1[i]-nums2[i])
        #     record[nums2[i]]=max(record[nums2[i]],abs(nums1[i]-nums2[i]))
        # for num in record:
        #     l=record[num]
        #     for s in range(-l+1,l):
        #         memo[num+s]=max(memo[num+s],l-abs(s))
        # temp=0
        # for x in nums1:
        #     temp=max(temp,memo[x])
        #     print(temp,x)
        # return (ans-temp)%(10**9+7)
        n=len(nums1)
        import collections
        memo=collections.defaultdict(int)
        records=collections.defaultdict(int)
        ans = 0
        for i in range(n):
            ans+=abs(nums1[i]-nums2[i])
            if abs(nums1[i]-nums2[i])>abs(records[nums2[i]]):
                records[nums2[i]]=nums1[i]-nums2[i]
        record=0
        for num in records:
            record=max(record,memo[num+records[num]])
            temp=abs(records[num])
            if temp>record:
                for j in range(record-temp+1,temp-record):
                    memo[num+j]=max(memo[num+j],temp-abs(j))
        temp=0
        for num in nums1:
            temp=max(memo[num],temp)
        return ans-temp

x=Solution()
print(x.minAbsoluteSumDiff(a,b))
