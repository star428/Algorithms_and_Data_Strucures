'''
Author: star428
Date: 2020-08-18 09:49:26
LastEditTime: 2020-08-18 10:02:50
LastEditors: Please set LastEditors
Description: 希尔排序的实现
FilePath: \Algorithms_and_Data_Strucures\chapter_5\shellSort.py
'''


def shellSort(alist):
    sublistCount = len(alist) // 2  # 无论奇偶第一步都会变成偶数
    while sublistCount > 0:
        for startPosition in range(sublistCount):
            gapInsertSort(alist, startPosition, sublistCount)

        print("After increments of size", sublistCount, "the list is", alist)

        sublistCount = sublistCount // 2


def gapInsertSort(alist, startPosition, gap):
    for index in range(startPosition + gap, len(alist), gap):
        currentValue = alist[index]
        position = index

        while position >= gap and \
                alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position -= gap

        alist[position] = currentValue


# test
shellSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
