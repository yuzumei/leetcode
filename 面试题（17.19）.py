import math
nums=[2,3,4,6]
sums=0
sumsquare=0
n=len(nums)+2
for x in nums:
    sums+=x
    sumsquare+=x*x
a=(n*n+n)/2-sums
b=(n*(n+1)*(2*n+1))/6-sumsquare
c=math.sqrt(abs(2*b-a*a))
print([int((a+c)/2),int((a-c)/2)])