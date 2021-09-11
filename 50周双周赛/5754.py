class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)-2):
            ss = s[i:i+3]
            if ss[0] != ss[1] and ss[1] != ss[2] and ss[0] != ss[2]:
                cnt += 1
        return cnt