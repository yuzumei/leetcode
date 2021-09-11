intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
class Solution:
    def insert(self, intervals, newInterval):
        ans=[]
        for item in intervals:
            ans.append(item)
            while ans[-1]!=newInterval and ans[-1][0]<=newInterval[1] and ans[-1][1]>=newInterval[0]:
                temp=ans.pop()
                newInterval=[min(temp[0],newInterval[0]),max(temp[1],newInterval[1])]
                while ans[-1][0]==newInterval[0]:
                    ans.pop()
                ans.append(newInterval)
        return ans
        # left, right = newInterval
        # placed = False
        # ans = list()
        # for li, ri in intervals:
        #     if li > right:
        #         # 在插入区间的右侧且无交集
        #         if not placed:
        #             ans.append([left, right])
        #             placed = True
        #         ans.append([li, ri])
        #     elif ri < left:
        #         # 在插入区间的左侧且无交集
        #         ans.append([li, ri])
        #     else:
        #         # 与插入区间有交集，计算它们的并集
        #         left = min(left, li)
        #         right = max(right, ri)
        #
        # if not placed:
        #     ans.append([left, right])
        # return ans
x=Solution()
print(x.insert(intervals,newInterval))