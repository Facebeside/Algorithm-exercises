'''
栈的抽象数据类型：
Stack():创建一个空栈。不需要参数，返回一个空栈。
push(item):将一个元素添加到栈的顶端。需要一个参数item,无返回值。
pop():将栈顶端的元素移除。不需要参数，返回顶端元素，并修改栈的内容。
peek():返回栈顶端的元素。不需要参数，返回顶端元素，不会修改栈的内容。
isEmpty():检查栈是否为空。不需要参数，返回布尔值。
size():返回栈中元素的个数。不需要参数，返回一个整数。
'''

# 假设列表的尾端是栈的顶端，入栈时新的元素被添加在列表的尾部
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

# 假设列表的头部是栈的顶端，入栈时元素被添加在列表的头部

class Stack2:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
    # s = Stack2()
    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    print(s.size())
    print(s.isEmpty())