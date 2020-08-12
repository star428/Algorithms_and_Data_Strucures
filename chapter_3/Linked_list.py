'''
Author: star428
Date: 2020-08-10 15:06:37
LastEditTime: 2020-08-11 11:07:49
LastEditors: Please set LastEditors
Description: 关于无序列表链表的实现
FilePath: \Algorithms_and_Data_Strucures\chapter_3\Linked_list.py
'''


class Node():  # 节点类
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:  # 无序列表类
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):  # 头节点添加
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0

        while current != None:
            current = current.getNext()
            count += 1
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def insert(self, index, item):
        current = self.head
        previous = None
        pos = 0
        while pos != index:
            previous = current
            current = current.getNext()
            pos += 1

        newNode = Node(item)
        if previous == None:
            newNode.setNext(current)
            self.head = newNode
        else:
            previous.setNext(newNode)
            newNode.setNext(current)

    def index(self, item):
        pos = 0
        current = self.head
        while item != current.getData():
            current = current.getNext()
            pos += 1
        return pos

    def append(self, item):
        current = self.head
        newNode = Node(item)
        if current != None:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newNode)
        else:
            self.head = newNode

    def pop(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        if previous == None:
            self.head = None
        else:
            previous.next = None


class OrderedList(UnorderedList):
    def __init__(self) -> None:
        super().__init__()

    def search(self, item):
        current = self.head
        stop = False
        found = False
        while current != None and not found and not stop:
            if item == current.data:
                found = True
            else:
                if current.data > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.data > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        newNode = Node(item)
        if previous == None:
            newNode.setNext(self.head)
            self.head = newNode
        else:
            newNode.setNext(current)
            previous.setNext(newNode)


# test
orderlist = OrderedList()
orderlist.add(10)
orderlist.add(11)
orderlist.add(9)
orderlist.add(13)
orderlist.pop()
print(orderlist.search(9))