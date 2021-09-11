class Solution:
    def trap(self, height) -> int:
        n=len(height)
        l,r=0,n-1
        ans=0
        lm,rm=height[l],height[r]
        while l<r:
            if lm<=rm:
                ans+=(max(0,lm-height[l]))
                l+=1
                lm=max(lm,height[l])
            else:
                ans+=(max(0,rm-height[r]))
                r-=1
                rm=max(rm,height[r])
        return ans

x=Solution()
print(x.trap([1,2]))

