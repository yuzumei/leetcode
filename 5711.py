class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        if n==1:
            return maxSum
        left=index
        right=n-1-index
        ans=1
        tempmin=n
        # tempmax=n+(left*(left+1))/2+(right*(right+1))/2
        while tempmin<=maxSum:
            if ans<=right or ans<=left:
                tempmin+=(min(ans-1,left)+min(ans-1,right)+1)
                ans+=1
            else:
                return (maxSum-tempmin)//n+ans
        return ans-1
x=Solution()
print(x.maxValue(8,7,14))
print(x.maxValue(4,2,6))
print(x.maxValue(6,1,10))
print(x.maxValue(3,2,18))
print(x.maxValue(4,0,4))