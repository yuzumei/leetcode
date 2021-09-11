class Solution:
    def getNumberOfBacklogOrders(self, orders) -> int:
        buy=[]
        sell=[]
        for order in orders:
            price=order[0]
            num=order[1]
            if order[2]==0:
                while sell and sell[0][0]<=price and num!=0:
                    if sell[0][1]<num:
                        num-=sell[0][1]
                        sell.pop(0)
                    else:
                        sell[0][1]-=num
                        num=0
                if num!=0:
                    if not buy or price<=buy[-1][0]:
                        buy.append([price,num])
                    else:
                        i=0
                        while buy[i][0]>price:
                            i+=1
                        buy.insert(i,[price,num])
            else:
                while buy and buy[0][0]>=price and num!=0:
                    if buy[0][1]<num:
                        num-=buy[0][1]
                        buy.pop(0)
                    else:
                        buy[0][1]-=num
                        num=0
                if num!=0:
                    if not sell or price>=sell[-1][0]:
                        sell.append([price,num])
                    else:
                        i=0
                        while sell[i][0]<price:
                            i+=1
                        sell.insert(i,[price,num])
        ans=0
        for item in buy:
            ans+=item[1]
        for item in sell:
            ans+=item[1]
        return ans%(10**9+7)
x=Solution()
print(x.getNumberOfBacklogOrders([[10,5,0],[15,2,1],[25,1,1],[30,4,0]]))