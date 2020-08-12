'''
Author: star428
Date: 2020-08-10 09:48:01
LastEditTime: 2020-08-10 10:12:04
LastEditors: Please set LastEditors
Description: 模拟打印任务
FilePath: \Algorithms_and_Data_Strucures\chapter_3\simulation_print_queue.py
'''
from random import randint
from print_queue import Printer, Task
from A_queue import Queue


def simulation(numSeconds, pagesPerMiunte):  # 设置总时间和打印机每分钟打印时间
    labPrinter = Printer(pagesPerMiunte)  #设置打印机
    printQueue = Queue()  # 打印队列
    waittingTimes = []  #每一个任务的等待时间构成的队列

    for current_second in range(numSeconds):
        if newPrintTask():  # 有没有新项目产生
            task = Task(current_second)
            printQueue.enqueue(task)

        if (not labPrinter.busy()) and \
            (not printQueue.isEmpty()):#不忙队列不空加入打印机打印
            nextTask = printQueue.dequeue()
            waittingTimes.append( \
                nextTask.waitTime(current_second))
            labPrinter.startNext(nextTask)

        labPrinter.tick()

    averageWait = sum(waittingTimes) / len(waittingTimes)
    print("Average Wait %6.2f secs %3d tasks remaining."\
        %(averageWait, printQueue.size()))


def newPrintTask():  # 模拟平均180秒产生一个项目
    num = randint(1, 181)
    if num == 180:
        return True
    else:
        return False


for num in range(10):
    simulation(3600, 5)
