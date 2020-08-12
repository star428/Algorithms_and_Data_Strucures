'''
Author: star428
Date: 2020-08-08 08:50:42
LastEditTime: 2020-08-08 09:33:45
LastEditors: Please set LastEditors
Description: 描述栈的一个类
FilePath: \Algorithms_and_Data_Strucures\chapter_3\stack.py
'''


class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)
