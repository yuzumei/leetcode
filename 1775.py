nums1 = [1,1,2,2,2,2]
nums2 = [1,2,3,4,5,6]
class Solution:
    def minOperations(self, nums1, nums2) -> int:
        n=len(nums1)
        m=len(nums2)
        if n>6*m or m>6*n:
            return -1
        gap=sum(nums1)-sum(nums2)
        if gap<0:
            nums1,nums2=nums2,nums1
            gap=-gap
        nums1.sort()
        nums2.sort()
        def count(num1,num2,gap):
            if gap==0:
                return 0
            if num1[-1]-1>6-num2[0]:
                temp=num1.pop()
                if gap<=temp-1:
                    return 1
                num1.insert(0,1)
                return 1+count(num1,num2,gap-temp+1)
            else:
                temp=num2.pop(0)
                if gap<=6-temp:
                    return 1
                num2.append(6)
                return 1+count(num1,num2,gap-6+temp)
        return count(nums1,nums2,gap)
x=Solution()
print(x.minOperations(nums1,nums2))
