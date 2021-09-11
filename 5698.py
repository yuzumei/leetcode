nums = [1,-1,1]
limit = 3
goal = -4
class Solution:
    def minElements(self, nums, limit: int, goal: int) -> int:
        sums=sum(nums)
        return abs(goal-sums)//limit+1 if abs(goal-sums)%limit!=0 else abs(goal-sums)//limit