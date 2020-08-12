'''
Author: star428
Date: 2020-08-11 14:31:46
LastEditTime: 2020-08-11 15:20:56
LastEditors: Please set LastEditors
Description: 洗车模拟
FilePath: \Algorithms_and_Data_Strucures\chapter_3\wash_the_car.py
'''
"""
    需求：完成一个洗车模拟，自动洗车站洗一个车需要5分钟，总共的等待
    位置只有5个，试计算在一个小时内洗车平均的等待时间
"""
from random import randint
from A_queue import Queue


class WashStation:
    def __init__(self, washSpeed):
        self.washSpeed = washSpeed  # 到时候给值0.2
        self.currentCar = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentCar != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentCar = None

    def isbusy(self):
        if self.currentCar != None:
            return True
        else:
            return False

    def startNext(self, car):
        self.currentCar = car
        self.timeRemaining = 1 / self.washSpeed


class Car:
    def __init__(self, time):
        self.timeStamp = time

    def getStamp(self):
        return self.timeStamp

    def waitForTime(self, currentTime):
        return currentTime - self.timeStamp


def simulation(numMinutes, washSpeed):
    washStation = WashStation(washSpeed)
    waittingQueue = Queue()
    waittingTime = []

    for current_minute in range(numMinutes):
        if waittingQueue.size() <= 5 and newCar():
            car = Car(current_minute)
            waittingQueue.enqueue(car)

        if (not washStation.isbusy()) and \
            (not waittingQueue.isEmpty()):
            nextcar = waittingQueue.dequeue()
            waittingTime.append(\
                nextcar.waitForTime(current_minute))
            washStation.startNext(nextcar)

        washStation.tick()

    averageWait = sum(waittingTime) / len(waittingTime)
    print("Average Wait %6.2f miuntes %3d cars remaining."\
        %(averageWait, waittingQueue.size()))


def newCar():
    num = randint(1, 6)
    if num == 5:
        return True
    else:
        return False

for num in range(10):
    simulation(60, 0.2)
