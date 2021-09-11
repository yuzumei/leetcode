'''堆heap'''
class MedianFinder:

    def __init__(self):
        self.maxitem=[]
        self.minitem=[]

    def addNum(self, num: int) -> None:
        if len(self.minitem)==0:
            self.minitem.append(num)
        else:
            if len(self.minitem)-len(self.maxitem)==0:
                if num>self.minitem[-1]:
                    self.minitem.insert(0,num)
                else:
                    self.minitem.append(num)
            else:


    def findMedian(self) -> float:
