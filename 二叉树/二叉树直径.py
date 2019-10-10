from binarytree import Node
from binarytree import build

# binarytree库中对二叉树的定义如下：
# class Node(object):

#     def __init__(self, value, left=None, right=None):
#         self.value = value  # The node value
#         self.left = left    # Left child
#         self.right = right  # Right child


class Solution:
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
            # 当前节点的高度
            num = max(left, right) + 1
            re = [self.dia, num]
            print(re)
            return num
        
        depth(root)
        return self.dia

if __name__ == '__main__':
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    values = [1,2,3,4,5]
    root = build(values)
    print(root)
    print("[当前结点的最大直径，当前节点的高度]:")
    solution = Solution()
    result = solution.diameterOfBinaryTree(root)
    print("二叉树的直径:")
    print(result)