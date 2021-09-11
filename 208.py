class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root={}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp=self.root
        for alpha in word:
            if alpha not in temp:
                temp[alpha]={}
            temp=temp[alpha]
        temp['leaf']=word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp=self.root
        for c in word:
            if c not in temp:
                return False
            temp=temp[c]
        return 'leaf' in temp

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp=self.root
        for c in prefix:
            if c not in temp:
                return False
            temp=temp[c]
        return len(temp)!=0