numCourses = 3
prerequisites = [[1,0],[0,1],[2,1],[0,2]] #[0,1]表示要学0 先学1
import collections
edges=collections.defaultdict(list)
indegree=[0]*numCourses
for item in prerequisites:
    edges[item[1]].append(item[0])
    indegree[item[0]]+=1
queue=[i for i in range(numCourses) if indegree[i]==0]
visited=0
while queue:
    visited+=1
    temp=queue.pop(0)
    for s in edges[temp]:
        indegree[s]-=1
        if indegree[s]==0:
            queue.append(s)
return visited==numCourses
# while q:
#     visited += 1
#     u = q.popleft()
#     for v in edges[u]:
#         indeg[v] -= 1
#         if indeg[v] == 0:
#             q.append(v)
#
# return visited == numCourses