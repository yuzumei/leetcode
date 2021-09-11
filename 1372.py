import collections
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        '''f(u)是根到节点u的路径上以u结尾且u为左儿子的最长路径，g为右儿子'''
        f=collections.defaultdict(int)
        g=collections.defaultdict(int)
        nodelist=[(root,None)]
        while nodelist:
            node,parent=nodelist.pop(0)
            if parent:
                if parent.left==node:
                    f[node]=g[parent]+1
                else:
                    g[node]=f[parent]+1
            if node.left:
                nodelist.append((node.left,node))
            if node.right:
                nodelist.append(node.right,node)
        ans=0
        for item in f:
            ans=max(ans,f[item])
        for item in g:
            ans=max(ans,g[item])
        return ans
        # f, g = collections.defaultdict(int), collections.defaultdict(int)
        # q = collections.deque([(root, None)])
        # while len(q) > 0:
        #     node, parent = q.popleft()
        #     if parent:
        #         if parent.left == node:
        #             f[node] = g[parent] + 1
        #         else:
        #             g[node] = f[parent] + 1
        #     if node.left:
        #         q.append((node.left, node))
        #     if node.right:
        #         q.append((node.right, node))
        #
        # maxans = 0
        # for _, val in f.items():
        #     maxans = max(maxans, val)
        # for _, val in g.items():
        #     maxans = max(maxans, val)
        # return maxans
