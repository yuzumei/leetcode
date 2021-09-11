nums = [1,4,3,7,4,5]
k = 0
class Solution:
    def maximumScore(self, nums: list, k: int) -> int:
        n=len(nums)
        memo=nums[k]
        l,r=k,k
        ans=nums[k]
        while l>-1 or r<n:
            print(l,r,memo)
            if l==-1:
                memo=memo if nums[r]>memo else nums[r]
                r+=1
            elif r==n:
                memo=memo if nums[l]>memo else nums[l]
                l-=1
            else:
                if nums[r]>=memo:
                    r+=1
                elif nums[l]>=memo:
                    l-=1
                else:
                    if nums[r]>nums[l]:
                        memo=nums[r]
                        r+=1
                    else:
                        memo=nums[l]
                        l-=1
            ans = max(ans, memo * (r - l - 1))
        return ans

x=Solution()
print(x.maximumScore(nums,k))