envelopes = [[5,4],[6,4],[6,7],[2,3]]
class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        def lengthOfLIS(nums):
            def search(list, num):
                left = 0
                right = len(list)
                while left < right:
                    mid = (left + right) // 2
                    if list[mid] == num:
                        return mid
                    elif list[mid] > num:
                        right = mid
                    else:
                        left = mid + 1
                return left

            d = [nums[0]]
            for num in nums:
                if num > d[-1]:
                    d.append(num)
                else:
                    indexnum = search(d, num)
                    d[indexnum] = num
                print(num, d)
            return len(d)

        if not envelopes:
            return 0
        n=len(envelopes)
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        temp=[envelopes[i][1] for i in range(n)]
        return lengthOfLIS(temp)
a=Solution()
print(a.maxEnvelopes(envelopes))
