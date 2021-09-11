class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals=[]
        self.index={}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.vals.append(val)
        if val not in self.index:
            self.index[val]=[len(self.vals)-1]
            return True
        else:
            self.index[val].append(len(self.vals)-1)
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.index:
            return False
        last=len(self.vals)-1
        idx=self.index[val].pop()
        if len(self.index[val])==0:
            del self.index[val]
        if last!=idx:
            self.vals[idx]=self.vals[last]
            self.index[self.vals[idx]].remove(last)
            self.index[self.vals[idx]].add(idx)
        self.vals.pop()
        return True

def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if self.vals:
            return self.vals[random.randint(0,len(self.vals)-1)]