'''
Author: star428
Date: 2020-08-10 09:22:43
LastEditTime: 2020-08-10 10:10:03
LastEditors: Please set LastEditors
Description: 用于构建打印模拟的printer类，task类
FilePath: \Algorithms_and_Data_Strucures\chapter_3\print_queue.py
'''
from A_queue import Queue
from random import randint


class Printer:
    def __init__(self, ppm) -> None:
        self.pagerate = ppm  # 每分钟打印多少页
        self.currentTask = None  # 是否有任务在打印，现在的任务
        self.timeRemaining = 0  # 打印的剩余时间

    def tick(self):  # 时间减一
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):  # 是否繁忙有任务
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = int(newtask.getPages() \
                            * 60 / self.pagerate) # 打印剩余时间


class Task:
    def __init__(self, time):
        self.timeStamp = time  # 时间戳
        self.pages = randint(1, 21)  # 页数随机

    def getStamp(self):
        return self.timeStamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):
        return currentTime - self.timeStamp