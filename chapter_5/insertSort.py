'''
Author: star428
Date: 2020-08-18 09:24:07
LastEditTime: 2020-08-18 09:34:02
LastEditors: Please set LastEditors
Description: 插入排序的一般实现
FilePath: \Algorithms_and_Data_Strucures\chapter_5\insertSort.py
'''


def insertSort(alist):
    for index in range(1, len(alist)):
        currentValue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentValue:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = currentValue


# test
insertSort([1, 2, 3, 43, 5, 6, 2, 1, 2, 4, 5])
