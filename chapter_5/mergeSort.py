'''
Author: star428
Date: 2020-08-18 17:39:29
LastEditTime: 2020-08-18 18:04:03
LastEditors: Please set LastEditors
Description: 归并排序的递归实现
FilePath: \Algorithms_and_Data_Strucures\chapter_5\mergeSort.py
'''
from random import randint


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        position_left = 0
        position_right = 0
        position_alist = 0

        while position_left < len(lefthalf) and \
                position_right < len(righthalf):
            if lefthalf[position_left] < righthalf[position_right]:
                alist[position_alist] = lefthalf[position_left]
                position_left += 1
            else:
                alist[position_alist] = righthalf[position_right]
                position_right += 1

            position_alist += 1

        while position_left < len(lefthalf):
            alist[position_alist] = lefthalf[position_left]
            position_left += 1
            position_alist += 1

        while position_right < len(righthalf):
            alist[position_alist] = righthalf[position_right]
            position_right += 1
            position_alist += 1


# test
alist = []
for num in range(20):
    num = randint(1, 100)
    alist.append(num)
print(alist)
mergeSort(alist)
print(alist)