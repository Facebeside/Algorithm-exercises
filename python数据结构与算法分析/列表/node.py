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


"""
构建无序链表：使用链表
add(item):假设元素item不在列表中，向列表中添加一个item，无返回值
remove(item)：移除item，无返回值，会修改列表
search(item)：搜索item，返回布尔值
isEmpty()：检查列表是否为空
length()：列表中元素个数
append(item):在列表最后添加一个item
index(item):返回item在列表中的位置
insert(pos, item)：在位置pos处添加item
pop():移除列表中最后一个元素
"""

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

    def getItem(self, index):
        current = self.head
        i = 0
        while i < index:
            current = current.getNext()
            i += 1
        return current.getDate()

    def insert(self, pos, item):
        temp = Node(item)
        current = self.head
        i = 0
        if pos == 0:
                temp.setNext(self.head)
                self.head = temp
        else:
            while i < pos-1:
                current = current.getNext()
                i += 1
            nextitem = current.getNext()
            temp.setNext(nextitem)
            current.setNext(temp)
                        
    def pop(self):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getNext() == None:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            data = current.getDate()
            previous.setNext(None)
            return data

"""
构建有序链表：使用链表
add(item):假设元素item不在列表中，向列表中添加一个item，无返回值
remove(item)：移除item，无返回值，会修改列表
search(item)：搜索item，返回布尔值
isEmpty()：检查列表是否为空
length()：列表中元素个数
append(item):在列表最后添加一个item
index(item):返回item在列表中的位置
insert(pos, item)：在位置pos处添加item
pop():移除列表中最后一个元素
"""

class OrderedList:
    def __init__(self):
        self.head = None
    
    # 检查链表是否为空
    def isEmpty(self):
        return self.head == None


    def length(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()
        
        return count

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

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getDate() == item:
                found = True
            else:
                if current.getDate() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getDate() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        
        temp = Node(item)
        if previous == None:
            temp.setNext(current)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)