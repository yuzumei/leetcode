class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class OperationTree:
    def insert(self, root, val):
        if root is None:
            root = TreeNode(val)

        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    def printTree(self, root):
        if root is None:
            return
        self.printTree(root.left)
        print(root.val, end=' ')
        self.printTree(root.right)

    def query(self, root):
        if root is None:
            return
        if val == root.val:
            return True
        elif val < root.val:
            self.query(root.left)
        elif val > root.right:
            self.query(root.right)

    def find_min(self, root):
        if root.left:
            return self.find_min(root.left)
        else:
            return root

    def find_max(self, root):
        if root.right:
            return self.find_max(root.right)
        else:
            return root

    def del_node(self, root, val):
        if root is None:
            return
        if val < root.val:
            root.left = self.del_node(root.left, val)
        elif val > root.val:
            root.right = self.del_node(root.right, val)
        # 当val == root.val时，分为三种情况：只有左子树或者只有右子树、有左右子树、即无左子树又无右子树
        else:
            if root.left and root.right:
                # 既有左子树又有右子树，则需找到右子树中最小值节点
                temp = self.find_min(root.right)
                root.val = temp.val
                # 再把右子树中最小值节点删除，让它符合二叉搜索树的定义
                root.right = self.del_node(root.right, temp.val)
            elif root.right is None and root.left is None:
                # 左右子树都为空
                root = None
            elif root.right is None:
                # 只有左子树
                root = root.left
            elif root.left is None:
                # 只有右子树
                root = root.right
        return root


if __name__ == '__main__':
    List = [17, 5, 35, 2, 11, 29, 38, 7,9, 16, 8]
    root = None
    op = OperationTree()
    for val in List:
        root = op.insert(root, val)
    op.del_node(root,5)
    print('中序打印二叉搜索树：', end=' ')
    op.printTree(root)