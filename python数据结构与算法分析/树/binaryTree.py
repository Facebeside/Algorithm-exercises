"""
二叉树的抽象数据类型：
BinaryTree()：创建一个二叉树的实例
getLeftChild():返回当前节点的左子节点所对应的二叉树
getRightChild():返回当前节点的右子节点所对应的二叉树
setRootVal(val):在当前节点中存储参数val中的对象
getRootVal()：返回当前节点存储的对象
insertLeft(val)：新建一颗二叉树，并将其作为当前节点的左子节点
insertRight(val)：新建一颗二叉树，并将其作为当前节点的右子节点
"""

'''
创建方式：列表之列表
'''
def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root, newBranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root

def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


'''
创建方式：
节点与引用
'''
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(rootObj)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(rootObj)
            t.rightChild = self.rightChild
            self.rightChild  = t

    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key