'''
Author: star428
Date: 2020-08-16 08:13:16
LastEditTime: 2020-08-16 08:41:18
LastEditors: Please set LastEditors
Description: 二分搜索的递归与非递归写法
FilePath: \Algorithms_and_Data_Strucures\chapter_5\mid_search.py
'''


# 非递归写法
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if alist[mid] == item:
            found = True
        else:
            if alist[mid] < item:
                first = mid + 1
            else:
                last = mid - 1

    return found


# 递归算法
def recursion_binarySearch(alist, item):
    if len(alist) == 1:
        if alist[0] == item:
            return True
        else:
            return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if alist[mid] < item:
                return recursion_binarySearch(alist[mid + 1:], item)
            else:
                return recursion_binarySearch(alist[:mid], item)


# test
binarySearch([1, 4, 7, 9, 10, 14, 16], 1)
print(recursion_binarySearch([1, 4, 7, 9, 10, 14, 16], 1))