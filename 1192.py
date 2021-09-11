class Solution:
    def criticalConnections(self, n: int, connections):
        '''初版'''
        # import collections
        # import copy
        # indeg=collections.defaultdict(list)
        # for item in connections:
        #     indeg[item[0]].append(item[1])
        #     indeg[item[1]].append(item[0])
        # memo=copy.deepcopy(indeg)
        # visited=collections.defaultdict(int) #0没走 1走了 2已经成环
        # path=[]
        # while len(indeg)>0:
        #     if not path:
        #         x=list(indeg.keys())[0]
        #         path.append(x)
        #         visited[x]=1
        #     else:
        #         x=path[-1]
        #         if not indeg[x]:
        #             del indeg[x]
        #             path.pop()
        #         else:
        #             target=indeg[x].pop(0)
        #             indeg[target].remove(x)
        #             path.append(target)
        #             if visited[target]==2 and visited[x]==2:
        #                 continue
        #             else:
        #                 if visited[target]==0:
        #                     visited[target]=1
        #                 else:
        #                     s=len(path)-2
        #                     while s>=0 and path[s]!=target:
        #                         visited[path[s]]=2
        #                         s-=1
        #                     visited[target]=2
        # ans=collections.defaultdict(set)
        # for item in visited:
        #     if visited[item]!=2:
        #         for s in memo[item]:
        #             ans[min(s,item)].add(max(s,item))
        # res=[]
        # for item in ans:
        #     for l in ans[item]:
        #         res.append([item,l])
        # return res

'''darjan算法'''
        

x=Solution()
print(x.criticalConnections(n = 5, connections = [[1,0],[2,0],[3,0],[4,1],[4,2],[4,0]]))