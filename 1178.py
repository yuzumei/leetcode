words = ["aaaa","asas","able","ability","actt","actor","access"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]

def subset(words):
    res=[""]
    for i in words:
        res = res + [i + word for word in res]
    return res
import collections
freq=collections.Counter()
for word in words:
    mask=0
    for c in word:
        mask|=1<<(ord(c)-ord('a'))
    freq[mask]+=1
res=[]
for puzzle in puzzles:
    ans=0
    for perm in subset(puzzle[1:]):
        mask=1<<(ord(puzzle[0])-ord('a'))
        for c in perm:
            mask|=1<<(ord(c)-ord('a'))
        ans+=freq[mask]
    res.append(ans)
print(res)
#         for puzzle in puzzles:
#             total = 0
#             for perm in self.subsets(puzzle[1:]):
#                 mask = 1 << (ord(puzzle[0]) - ord('a'))
#                 for c in perm:
#                     mask |= 1 << (ord(c) - ord('a'))
#                 total += freq[mask]
#             res.append(total)
#         return res
#
#     def subsets(self, words: List[int]) -> List[List[int]]:
#         res = [""]
#         for i in words:
#             res = res + [i + word for word in res]
#         return res


'''单词word要包含谜面第一个字 单词中每一个字都要在谜面内'''
import collections
alpha='qwertyuiopasdfghjklzxcvbnm'
prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
diff={alpha[i]:prime[i] for i in range(26)}
def alphatonum(word):
    ans=1
    for item in word:
        ans*=diff[item]
    return ans
wordsnum=collections.defaultdict(int)
puzzles1=[]
puzzlesnum=[]
for word in words:
    temp=set(word)
    wordsnum[alphatonum(temp)]+=1
for puzzle in puzzles:
    puzzles1.append(diff[puzzle[0]])
    puzzlesnum.append(alphatonum(puzzle))
ans=[]
for i in range(len(puzzlesnum)):
    res=0
    for item in wordsnum:
        if item%puzzles1[i]==0 and puzzlesnum[i]%item==0:
            res+=wordsnum[item]
    ans.append(res)
print(ans)

# wordsset=[set(item) for item in words]
# from collections import defaultdict
# memopuzzle=[]
# for item in puzzles:
#     temp=defaultdict(int)
#     for i in item:
#         temp[i]+=1
#     memopuzzle.append(temp)
# ans=[]
# for i in range(len(puzzles)):
#     res=0
#     for item in wordsset:
#         flag=1
#         if puzzles[i][0] not in item:
#             continue
#         for alpha in item:
#             if memopuzzle[i][alpha]==0:
#                 flag=0
#                 break
#         if flag==1:
#             res+=1
#     ans.append(res)
#
# print(ans)
'''超时'''