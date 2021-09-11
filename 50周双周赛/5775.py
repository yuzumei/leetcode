class Solution:
    def minSkips(self, dist, speed: int, hoursBefore: int) -> int:
        if sum(dist)//speed > hoursBefore:
            return -1

