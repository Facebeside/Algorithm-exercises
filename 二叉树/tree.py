from binarytree import Node
from binarytree import build

# binarytree库中对二叉树的定义如下：
# class Node(object):

#     def __init__(self, value, left=None, right=None):
#         self.value = value  # The node value
#         self.left = left    # Left child
#         self.right = right  # Right child


class Solution:

    # 二叉树的深度

    def maxDepth(self, root):   
        if not root:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left,right) + 1
        
    # 二叉树的直径

    def diameterOfBinaryTree(self,root):
        
        # 深度优先遍历       
        self.dia = 0
        def depth(node):
            if not node:
                return 0
            
            left = depth(node.left)
            right = depth(node.right)
            # 当前最大的直径
            self.dia = max(left + right, self.dia)
            # 当前节点的深度
            num = max(left, right) + 1
            re = [self.dia, num]
            print(re)
            return num
        
        depth(root)
        return self.dia

    # 翻转二叉树

    def invertTree(self, root):

        if root != None:
            node = root
            left = self.invertTree(node.left)
            right = self.invertTree(node.right)
            node.left = right
            node.right = left
        else:
            return None
        return node

if __name__ == '__main__':
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    values = [3,9,20,None,None,15,7]
    root = build(values)
    print(root)
    print("[当前结点的最大直径，当前节点的高度]:")
    solution = Solution()
    result = solution.diameterOfBinaryTree(root)
    print("二叉树的直径:",result)
    length = solution.maxDepth(root)
    print("二叉树的深度为：" ,length)
    print("翻转之后的二叉树为：",solution.invertTree(root))    