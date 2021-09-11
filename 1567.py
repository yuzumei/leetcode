class Solution:
    def getMaxLen(self, nums) -> int:
        nums.append(0)
        ans,temp,start,end=0,[],-1,-1
        for i,num in enumerate(nums):
            if num!=0 and start==-1:
                start=i
            if num<0:
                temp.append(i)
            elif num==0:
                if start!=-1:
                    end=i-1
                    if len(temp)%2==0:
                        ans=max(ans,end-start+1)
                    else:
                        ans=max(ans,end-temp[0],temp[-1]-start)
                temp, start, end = [], -1, -1
            print(temp,start,end)
        return ans
x=Solution()
print(x.getMaxLen([0,-19,26,-24,-13,-2,26,10,0,4,0,-26,-22,9,35,-11,-14,0,-29]))