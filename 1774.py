baseCosts = [2,3]
toppingCosts = [4,5,100]
target = 18
class Solution:
    def closestCost(self, baseCosts, toppingCosts, target: int):
        ans = baseCosts[0]  # 初始化一个方案（不添加任何配料）
        # 枚举，将所有可能的方案加入li，共len(baseCosts)*3^len(toppingCosts)种
        li = baseCosts
        for cost in toppingCosts:
            for c in li.copy():
                li.append(c + cost)
                li.append(c + 2 * cost)
        # 遍历一遍所有方案，找到最接近target且成本相对较低的方案
        for a in li:
            if abs(a - target) < abs(ans - target) or abs(a - target) == abs(ans - target) and a < ans:
                ans = a
        return ans



x=Solution()
print(x.closestCost(baseCosts,toppingCosts,target))
