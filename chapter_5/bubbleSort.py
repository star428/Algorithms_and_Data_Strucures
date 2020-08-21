'''
Author: star428
Date: 2020-08-17 10:55:39
LastEditTime: 2020-08-17 11:08:26
LastEditors: Please set LastEditors
Description: 冒泡排序一般实现及其改良
FilePath: \Algorithms_and_Data_Strucures\chapter_5\bubbleSort.py
'''


def bubbleSort(numList):
    for Outnum in range(len(numList) - 1, 0, -1):
        for inNum in range(Outnum):
            if numList[inNum] > numList[inNum + 1]:
                numList[inNum], numList[inNum + 1] = numList[inNum +1],\
                    numList[inNum]


def shortBubbleSort(numList):
    exchanges = True
    passnum = len(numList) - 1
    while passnum != 0 and exchanges:
        exchanges = False
        for num in range(passnum):
            if numList[num] > numList[num + 1]:
                numList[num], numList[num + 1] = numList[num + 1], numList[num]
                exchanges = True
        passnum -= 1


# test
numList = [1, 4, 2, 23, 6, 8, 4, 21, 65, 7, 67]
# bubbleSort(numList)
shortBubbleSort(numList)