tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
'''超时'''
# ans=[]
# n=len(tickets)
# def dfs(res,tickets):
#     if not tickets:
#         ans.append(res)
#     else:
#         for i in range(len(tickets)):
#             if tickets[i][0]==res[-1]:
#                 temp=res+[tickets[i][1]]
#                 dfs(temp,tickets[:i]+tickets[i+1:])
#
# dfs(["JFK"],tickets)
# print(sorted(ans)[0])
from collections import defaultdict
startend=defaultdict(list)
for item in tickets:
    startend[item[0]].append(item[1])
for item in startend:
    startend[item].sort()
ans = []
def dfs(f):
    while startend[f]:
        dfs(startend[f].pop(0))
    ans.insert(0, f)
dfs('JFK')
print(ans)

