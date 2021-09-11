import heapq
class SeatManager:

    def __init__(self, n: int):
        self.res=list(range(1,n+1))
        heapq.heapify(self.res)

    def reserve(self) -> int:
        return heapq.heappop(self.res)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.res,seatNumber)