class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        import collections
        memo=collections.defaultdict(list)
        def search(node,i):
            if not node:
                return
            memo[i].append(node)
            search(node.left,i+1)
            search(node.right,i+1)
        ans=[]
        for i in memo:
            ans+=memo[i]
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        ans=TreeNode(-10001)
        ans.left=TreeNode(data[0])
        queue=[TreeNode(data[0])]
        n=len(data)
        i=0
        while i<n:
            target=queue.pop(0)
            i+=1
            if not data[i]:
                target.left = TreeNode(data[i])
                queue.append(TreeNode(data[i]))
            i+=1
            if not data[i]:
                target.right = TreeNode(data[i])
                queue.append(TreeNode(data[i]))
        return ans.left