class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        if D==len(weights):
            return max(weights)
        ans=max(max(weights),sum(weights)//D)
        weights.append(0)
        while True:
            cnt,temp,record=0,0,float('inf')
            for num in weights:
                if cnt>D:
                    break
                if temp+num<=ans:
                    temp+=num
                else:
                    record=min(record,temp+num)
                    temp=num
                    cnt+=1
            cnt=cnt+1 if temp!=0 else cnt
            if cnt<=D:
                return ans
            else:
                ans=record
x=Solution()
print(x.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], D = 5))
print(x.shipWithinDays(weights = [3,2,2,4,1,4], D = 3))
print(x.shipWithinDays(weights = [1,2,3,1,1,1,1,1,1], D = 4))