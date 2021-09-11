import random
a,b,c=random.randint(1,10000),random.randint(1,10000),random.randint(1,10000)
for i in range(500):
    if not ((a&b)^(a&c)==a&(b^c)):
        print('1')

class Solution:
    def getXORSum(self, arr1, arr2) -> int:
        x,y=0,0
        for num in arr1:
            x^=num
        for num in arr2:
            y^=num
        return x&y
x=Solution()
print(x.getXORSum(arr1 = [1,2,3], arr2 = [6,5]))