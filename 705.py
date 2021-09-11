class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.memo=[[] for _ in range(1001)]

    def add(self, key: int) -> None:
        n=key%1000
        m=key-1000*n
        if len(self.memo[n])==0:
            self.memo[n]=[0]*1000
        self.memo[n][m]=1

    def remove(self, key: int) -> None:
        n=key%1000
        m=key-1000*n
        if len(self.memo[n])==0:
            return
        else:
            self.memo[n][m]=0

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        n=key%1000
        m=key-1000*n
        if len(self.memo[n])==0:
            return False
        else:
            return self.memo[n][m]==1