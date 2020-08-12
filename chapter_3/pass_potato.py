'''
Author: your name
Date: 2020-08-09 16:12:07
LastEditTime: 2020-08-10 09:06:23
LastEditors: Please set LastEditors
Description: 利用单端队列实现传土豆
FilePath: \Algorithms_and_Data_Strucures\chapter_3\pass_potato.py
'''
from A_queue import Queue
from random import randint


def hotPotato(namelist):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        random_num = randint(1, 10)

        for num in range(random_num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


# test
print(hotPotato(["sam", "lisa", "jack", "jon", "brown", "bule"]))
