"""
双端队列抽象数据类型
Deque():创建一个空的双端队列，不需要参数，返回一个空的双端队列
addFront(item):将一个元素插到双端队列的前端，有一个参数，没有返回值
addRear(item):将一个元素插到双端队列的后端，有一个参数，没有返回值
removeFront()：从前端移除一个元素，不需要参数，会返回一个元素，并修改队列内容
removeRear()：从后端移除一个元素，不需要参数，会返回一个元素，并修改队列内容
isEmpty():检查队列是否为空
size()：队列元素数目
"""

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

# 回文检测器
def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)
    
    stillEqual = True

    while chardeque.size > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()

        if first != last:
            stillEqual = False
    
    return stillEqual