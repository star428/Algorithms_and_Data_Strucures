'''
Author: star428
Date: 2020-08-12 09:44:41
LastEditTime: 2020-08-12 10:53:55
LastEditors: Please set LastEditors
Description: 基数排序器的实现
FilePath: \Algorithms_and_Data_Strucures\chapter_3\Radix_sort.py
'''
from A_queue import Queue
import copy
import random


def get_digit_length(queue):
    digitLength = 0
    test_queue = copy.deepcopy(queue)
    while not test_queue.isEmpty():
        num = str(test_queue.dequeue())
        if len(num) > digitLength:
            digitLength = len(num)

    return digitLength


def radix_sort(mainQueue):
    otherQueue = {str(num): Queue() for num in range(10)}
    digit = 0  # 表示位数

    for digit in range(get_digit_length(mainQueue)):
        
        while not mainQueue.isEmpty():
            num = str(mainQueue.dequeue())  # 转换为字符串解决位数计算问题
            if digit > (len(num) - 1):  # 计算的位数超出该数字的最大位数的时候
                otherQueue["0"].enqueue(int(num))
            else:
                otherQueue[num[len(num) - 1 - digit]].enqueue(int(num))

        for num in range(10):
            queue = otherQueue[str(num)]
            while not queue.isEmpty():
                mainQueue.enqueue(queue.dequeue())
    return mainQueue

# 测试
mainQueue = Queue()
for num in range(10):
    mainQueue.enqueue(random.randint(1, 200))
print(mainQueue.items)
mainQueue = radix_sort(mainQueue)
print(mainQueue.items)