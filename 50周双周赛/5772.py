class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a,b,c = '', '', ''
        for s in firstWord:
            a += str(ord(s)-ord('a'))
        for s in secondWord:
            b += str(ord(s)-ord('a'))
        for s in targetWord:
            c += str(ord(s)-ord('a'))
        return int(a)+int(b)==int(c)