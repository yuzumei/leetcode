class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minnum=[]

    def push(self, x: int) -> None:
        self.stack.append(x)
        while self.minnum and self.minnum[-1]>x:
            self.minnum.pop()

    def pop(self) -> None:
        temp=self.stack.pop()
        if temp==self.minnum[0]:
            self.minnum.pop(0)
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minnum[0]