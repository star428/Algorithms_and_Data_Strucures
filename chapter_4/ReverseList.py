'''
Author: star428
Date: 2020-08-13 11:39:08
LastEditTime: 2020-08-13 15:20:03
LastEditors: Please set LastEditors
Description: 列表反转递归实现
FilePath: \Algorithms_and_Data_Strucures\chapter_4\ReverseList.py
'''

stack = []


def reverseList(alist):
    if len(alist) > 1:
        stack.append(alist[-1])
        reverseList(alist[:-1])
    else:
        stack.append(alist[-1])


# test
print(reverseList([1, 2, 3, 4, 5]))
