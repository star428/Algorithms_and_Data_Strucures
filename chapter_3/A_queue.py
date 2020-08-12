'''
Author: star428
Date: 2020-08-09 15:56:10
LastEditTime: 2020-08-09 16:32:45
LastEditors: Please set LastEditors
Description: 描述队列的一个类
FilePath: \Algorithms_and_Data_Strucures\chapter_3\A_queue.py
'''


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
