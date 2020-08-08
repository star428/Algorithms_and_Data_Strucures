'''
Author: star428
Date: 2020-08-07 10:32:50
LastEditTime: 2020-08-07 15:53:33
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Algorithms_and_Data_Strucures\chapter_2\find_small_num.py
'''
import random
list_one = []
n = 1000
for num in range(n):
    list_one.append(random.randint(1, 20))

list_two = [11, 21, 33, 12]


# 归并排序,时间复杂度nlogn
def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        # 分治调用，调用到数组长度均为1时停止，此时就开始归并
        mergeSort(lefthalf)
        mergeSort(righthalf)
        # 此时为指向两边和最终的指针
        left_node = 0
        right_node = 0
        alist_node = 0
        # 两个list已排好序，按大小安排到一个list中
        while left_node < len(lefthalf) and right_node < len(righthalf):
            if lefthalf[left_node] < righthalf[right_node]:
                alist[alist_node] = lefthalf[left_node]
                left_node += 1
            else:
                alist[alist_node] = righthalf[right_node]
                right_node += 1
            alist_node += 1

        while left_node < len(lefthalf):
            alist[alist_node] = lefthalf[left_node]
            left_node += 1
            alist_node += 1

        while right_node < len(righthalf):
            alist[alist_node] = righthalf[right_node]
            right_node += 1
            alist_node += 1

    print("Merging ", alist)


mergeSort(list_two)
print(list_two)