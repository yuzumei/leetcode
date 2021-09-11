class Solution:
    def minimumXORSum(self, nums1, nums2) -> int:
        import math
        nums1.sort(reverse=True)
        nums2.sort(reverse=True)
        ans = 0
        while nums1 and nums2:
            nums1.sort(reverse=True)
            nums2.sort(reverse=True)
            if nums1[0] == 0 or nums2[0]==0:
                ans+=nums1.pop(0)^nums2.pop(0)
            else:
                m,n=int(math.log2(nums1[0])),int(math.log2(nums2[0]))
                if m>n:
                    nums1.append(nums1.pop(0)-2**m)
                    ans+=2**m
                elif m<n:
                    nums2.append(nums2.pop(0)-2**n)
                    ans+=2**n
                else:
                    a=0
                    memo,bb,cc=float('inf'),-1,-1
                    while a<len(nums1) and nums1[a]>=2**m:
                        i = 0
                        while i<len(nums2) and nums2[i]>=2**n:
                            if nums1[a]^nums2[i]<memo:
                                memo=nums1[a]^nums2[i]
                                bb=a
                                cc=i
                            i+=1
                        a+=1
                    nums1.pop(bb)
                    nums2.pop(cc)
                    ans+=memo
        return ans

x=Solution()
print(x.minimumXORSum(nums1 = [100,26,12,62,3,49,55,77,97], nums2 = [98,0,89,57,34,92,29,75,13]))