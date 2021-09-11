arr = [[1,2,3],[4,5,6],[7,8,9]]
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n=len(arr)
        first,firstindex,second=0,-1,0
        for i in range(n):
            tempfs,tempfsi,tempsec=float("inf"),-1,float("inf")
            for j in range(n):
                cursum=(first if firstindex!=j else second)+arr[i][j]
                if cursum<tempfs:
                    tempfs, tempfsi, tempsec = cursum,j,tempfs
                elif cursum<tempsec:
                    tempsec=cursum
            first, firstindex, second = tempfs,tempfsi,tempsec
        return first
        # n = len(arr)
        # first_sum, first_pos, second_sum = 0, -1, 0
        # for i in range(n):
        #     fs, fp, ss = 10**9, -1, 10**9
        #     for j in range(n):
        #         cur_sum = (first_sum if first_pos != j else second_sum) + arr[i][j]
        #         if cur_sum < fs:
        #             fs, fp, ss = cur_sum, j, fs
        #         elif cur_sum < ss:
        #             ss = cur_sum
        #     first_sum, first_pos, second_sum = fs, fp, ss
        # return first_sum
