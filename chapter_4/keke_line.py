'''
Author: star428
Date: 2020-08-14 17:29:49
LastEditTime: 2020-08-14 18:15:14
LastEditors: Please set LastEditors
Description: 科勒雪花递归实现
FilePath: \Algorithms_and_Data_Strucures\chapter_4\keke_line.py
'''
from turtle import Turtle
myTurtle = Turtle()
myWin = myTurtle.getscreen()
myTurtle.up()
myTurtle.setposition((-100, 0))
myTurtle.down()
myTurtle.speed(100)


def keke_line(myTurtle, n=1, length=120):  # n是阶数，length是0阶总长度
    if n == 0:
        myTurtle.fd(length)
    else:
        for rent in [0, 60, -120, 60]:  # 转一个三角形
            myTurtle.left(rent)
            keke_line(myTurtle, n - 1, length / 3)


def makeKekeWhite(myTurtle, n, length):
    for num in range(3):
        keke_line(myTurtle, 3, 240)
        myTurtle.right(120)


# test
makeKekeWhite(myTurtle, 3, 240)
myWin.exitonclick()
