"""
队列抽象数据类型
Queue():创建一个空队列。不需要参数，返回一个空队列
enqueue(item):在队列的尾部添加一个元素。需要参数，无返回值
dequeue():在队列头部移除一个元素。无参数，返回一个参数，会修改队列内容
isEmpty():判断队列是否为空，无参数，返回一个布尔值
size():返回队列中元素的数目。无参数，返回一个整数
"""


# 假设列表的0位置为队列的尾部，列表的尾部为队列的头
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)