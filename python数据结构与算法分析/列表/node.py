"""
构建无序链表：使用链表
"""

# Node类，链表的基本数据类型，包含数据元素和地址
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    
    def getDate(self):
        return self.data
    
    def getNext(self):
        return self.next

    def setDate(self, newdate):
        self.data = newdate
    
    def setNext(self, newnext):
        self.next = newnext


# 无序列表类，包含指向第一个节点的引用
class UnorderedList:
    def __init__(self):
        self.head = None

    # 检查链表是否为空
    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()
        
        return count
    
    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getDate() == item:
                found = True
            else:
                current = current.getNext()
        
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getDate() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        temp = Node(item)
        current = self.head
        found = False

        while not found:
            if current.getNext() == None:
                found = True
                temp.setNext(None)
                current.setNext(temp)
            else:
                current = current.getNext()

    def index(self, item):
        current = self.head
        found = False
        count = 0
        while not found:
            if current.getDate() == item:
                found = True
            else:
                current = current.getNext()
                count += 1
        
        return count

    # def pop(self):
    #     current = self.head
    #     previous = None
    #     found = False

    #     while not found:
    #         if current.getNext() == None:
    #             found = True
    #             data = current.getDate()
    #             previous.setNext(None)
    #             return data
    #         else:
    #             previous = current
    #             current = current.getNext()