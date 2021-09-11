nums = [10,9,2,5,3,7,101,18]
class Solution:
    def lengthOfLIS(self, nums) -> int:
        n=len(nums)
        # dp=[1]*n
        # for i in range(n):
        #     for j in range(i):
        #         if nums[i]>nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return dp[-1]
        def search(list,num):
            left=0
            right=len(list)
            while left<right:
                mid=(left+right)//2
                if list[mid]==num:
                    return mid
                elif list[mid]>num:
                    right=mid
                else:
                    left=mid+1
            return left

        d=[nums[0]]
        for num in nums:
            if num>d[-1]:
                d.append(num)
            else:
                indexnum=search(d,num)
                d[indexnum]=num
            print(num,d)
        return len(d)

a=Solution()
print(a.lengthOfLIS(nums))