
'''
python 实现的二叉树
包括递归和非递归的遍历二叉树
'''
# 树结构


class BTNode(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BTree(object):
    def __init__(self, dataSource, length):
        self._root = BTNode(dataSource[0])
        for x in range(1, length):
            node = BTNode(dataSource[x])
            self.insertElement(self.root, node)
    # 在一个节点插入子节点

    @property
    def root(self):
        if self._root:
            return self._root
        return None

    @root.setter
    def root(self, data):
        self._root = data

    def insertElement(self, root, node):
        if root:
            if node.data < root.data:  # 插入左侧 空则插入否则在其左子树中查找
                if root.leftChild:
                    self.insertElement(root.leftChild, node)
                else:
                    root.leftChild = node
            else:
                if root.rightChild:  # 插入右侧
                    self.insertElement(root.rightChild, node)
                else:
                    root.rightChild = node
    # 先序访问

    def PreorderTraversalBinaryTree(self, root):
        if root:
            print('%d | ' % root.data,)
            self.PreorderTraversalBinaryTree(root.leftChild)
            self.PreorderTraversalBinaryTree(root.rightChild)
    # 后序访问

    def PostorderTraversalBinaryTree(self, root):
        if root:
            self.PostorderTraversalBinaryTree(root.leftChild)
            self.PostorderTraversalBinaryTree(root.rightChild)
            print('%d | ' % root.data,)
    # 中序访问

    def MiddleTraversalBinaryTree(self, root):
        if root:
            self.MiddleTraversalBinaryTree(root.leftChild)
            print('%d | ' % root.data,)
            self.MiddleTraversalBinaryTree(root.rightChild)

    # 非递归实现 先序
    def preorderNoRecall(self, root):
        if root:
            retmp = []
            order = []
            retmp.append(root)
            while retmp:
                tNode = retmp.pop()
                order.append(tNode)
                print('%d | ' % tNode.data,)
                if tNode.rightChild:
                    retmp.append(tNode.rightChild)
                if tNode.leftChild:
                    retmp.append(tNode.leftChild)
            return order
    # 非递归 中序

    def midOrderNorecall(self, root):
        if root:
            retmp = []
            order = []
            retmp.append(root)
            while retmp:
                tNode = retmp[-1]
                if tNode.leftChild:
                    if tNode.leftChild in order:  # 若左边已经访问过则访问中间节点
                        tNode = retmp.pop()
                        order.append(tNode)
                        print('%d | ' % tNode.data,)
                        if tNode.rightChild:
                            retmp.append(tNode.rightChild)
                        continue
                    retmp.append(tNode.leftChild)
                    continue
                tNode = retmp.pop()
                order.append(tNode)
                print('%d | ' % tNode.data,)
                if tNode.rightChild:
                    retmp.append(tNode.rightChild)
    # 非递归后序

    def postOrderNorecall(self, root):
        if root:
            retmp = []
            order = []
            retmp.append(root)
            while retmp:
                tNode = retmp[-1]
                if tNode.rightChild:
                    if tNode.rightChild in order:
                        tNode = retmp.pop()
                        order.append(tNode)
                        print('%d | ' % tNode.data,)
                        continue
                    retmp.append(tNode.rightChild)
                if tNode.leftChild:
                    if tNode.leftChild in order:
                        tNode = retmp.pop()
                        order.append(tNode)
                        print('%d | ' % tNode.data,)
                        continue
                    retmp.append(tNode.leftChild)
                if not tNode.rightChild and not tNode.leftChild:
                    tNode = retmp.pop()
                    order.append(tNode)
                    print('%d | ' % tNode.data,)


if __name__ == '__main__':
    ls = [5, 1, 3, 2, 7, 8, 6, 4, 9]
    t = BTree(ls, len(ls))

    t.postOrderNorecall(t.root)
    print('-----')
    t.PostorderTraversalBinaryTree(t.root)
