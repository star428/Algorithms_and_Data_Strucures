'''
Author: star428
Date: 2020-08-10 10:18:15
LastEditTime: 2020-08-10 10:23:16
LastEditors: Please set LastEditors
Description: 双端队列实现类
FilePath: \Algorithms_and_Data_Strucures\chapter_3\deque.py
'''
class Deque:
    def __init__(self):
        self.items = []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)