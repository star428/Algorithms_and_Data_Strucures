'''
Author: star428
Date: 2020-08-12 16:04:12
LastEditTime: 2020-08-12 16:07:30
LastEditors: Please set LastEditors
Description: 绘制螺旋线
FilePath: \Algorithms_and_Data_Strucures\chapter_4\draw_spiral.py
'''
from turtle import *


def makeHelix():
    myTurtle = Turtle()
    myWindows = myTurtle.getscreen()

    def drawSpiral(myTurtle, lineLen):
        if lineLen > 0:
            myTurtle.forward(lineLen)
            myTurtle.right(90)
            drawSpiral(myTurtle, lineLen - 5)

    drawSpiral(myTurtle, 100)
    myWindows.exitonclick()


# test
makeHelix()