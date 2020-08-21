'''
Author: star428
Date: 2020-08-17 14:34:10
LastEditTime: 2020-08-17 14:52:08
LastEditors: Please set LastEditors
Description: 选择排序的一般递归实现
FilePath: \Algorithms_and_Data_Strucures\chapter_5\selectSort.py
'''

sortlist = []


def selectSort(alist):
    if len(alist) > 0:
        maxNum = 0
        for num in range(len(alist)):
            if alist[num] > alist[maxNum]:
                maxNum = num

        sortlist.insert(0, alist[maxNum])

        alist[maxNum], alist[len(alist) - 1] = \
        alist[len(alist) - 1], alist[maxNum]

        selectSort(alist[:-1])


# test
selectSort([2, 5, 1, 3, 2])
