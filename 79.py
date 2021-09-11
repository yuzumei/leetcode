board =[
     ["A", "B", "C", "E"],
     ["S", "F", "E", "S"],
     ["A", "D", "E", "E"]
]
class Solution:
    def exist(self, board, word: str):
        import collections
        import copy
        memo=collections.defaultdict(list)
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                memo[board[i][j]].append([i,j])
        self.ans=0
        def dfs(num,memodict,word):
            if not word:
                self.ans=1
                return
            temp=copy.deepcopy(memodict)
            print(num)
            tempnum=[[num[0]+1,num[1]],[num[0]-1,num[1]],[num[0],num[1]+1],[num[0],num[1]-1]]
            for nums in tempnum:
                if nums in temp[word[0]]:
                    temp[word[0]].remove(nums)
                    dfs(nums,temp,word[1:])
            return

        word1=word[1:]
        for num in memo[word[0]]:
            tempdict=copy.deepcopy(memo)
            tempdict[word[0]].remove(num)
            dfs(num,tempdict,word1)
            if self.ans==1:
                return True
        return False
a=Solution()
print(a.exist(board,"ABCESEEEFS"))


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break

            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False


