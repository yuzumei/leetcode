class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        l,r,memo,ans=0,0,-1,0
        n=len(word)
        record={'a':0,'e':1,'i':2,'o':3,'u':4}
        while r<n:
            if record[word[r]]==memo+1:
                memo = record[word[r]]
                r+=1
            elif record[word[r]]==memo:
                r+=1
            else:
                if memo==4:
                    ans=max(ans,r-l)
                if record[word[r]]!=0:
                    r+=1
                l=r
                memo=-1
        return max(ans,r-l) if memo==4 else ans
x=Solution()
print(x.longestBeautifulSubstring(word = "aou"))