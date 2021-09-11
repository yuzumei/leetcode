n = 6
edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
'''超时'''
import collections
memo=collections.defaultdict(list)
for item in edges:
    memo[item[0]].append(item[1])
    memo[item[1]].append(item[0])
ans=float('inf')
memoindex=[]
for item in memo:
    for i in range(len(memo[item])):
        if memo[item][i] in memoindex:
            continue
        else:
            for x in memo[item][i+1:]:
                temp=0
                if memo[item][i] in memo[x]:
                    temp += len(memo[item]) - 2
                    temp += len(memo[memo[item][i]]) - 2
                    temp += len(memo[x]) - 2
                    ans=min(temp,ans)
    memoindex.append(item)
print(ans)

        graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        degrees = [0 for _ in range(n + 1)]
        for i, j in edges:
            graph[i][j] = 1
            graph[j][i] = 1
            degrees[i] += 1
            degrees[j] += 1

        ans = float('inf')
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    if graph[i][j] and graph[i][k] and graph[j][k]:
                        ans = min(ans, degrees[i] + degrees[j] + degrees[k] - 6)
        return -1 if ans == float('inf') else ans
