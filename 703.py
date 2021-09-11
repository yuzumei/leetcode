class KthLargest:

    def __init__(self, k, nums):
        self.big=[]
        self.k=k
        for item in nums:
            flag = 0
            if len(self.big)==0:
                self.big.append(item)
            else:
                for i in range(len(self.big)):
                    if self.big[i]<item:
                        self.big.insert(i,item)
                        flag=1
                        break
                if flag==0:
                    self.big.append(item)
                if len(self.big)==k+1:
                    self.big.pop()

    def add(self, val):
        flag = 0
        if len(self.big) == 0:
            self.big.append(val)
        else:
            for i in range(len(self.big)):
                if self.big[i] < val:
                    self.big.insert(i,val)
                    flag = 1
                    break
            if flag == 0:
                self.big.append(val)
            if len(self.big) == self.k+1:
                self.big.pop()
        return self.big[-1]

a=KthLargest(3,[4, 5, 8, 2])
print(a.add(3))
print(a.add(5))
print(a.add(10))
print(a.add(9))
print(a.add(4))


