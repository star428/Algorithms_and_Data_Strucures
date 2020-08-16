'''
Author: star428
Date: 2020-08-13 11:04:01
LastEditTime: 2020-08-13 11:22:38
LastEditors: Please set LastEditors
Description: 绘制谢尔平斯基三角形
FilePath: \Algorithms_and_Data_Strucures\chapter_4\draw_triangle.py
'''

from turtle import Turtle


def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degreen, myTurtle):  # degreen为递减度
    colorMap = [
        "blue", "red", "yellow", "white", "green", "violet", "orange", "pink"
    ]
    drawTriangle(points, colorMap[degreen], myTurtle)
    if degreen > 0:
        sierpinski((points[0], getMid(
            points[0], points[1]), getMid(points[0], points[2])), degreen - 1,
                   myTurtle)
        sierpinski((getMid(
            points[0], points[1]), points[1], getMid(points[1], points[2])),
                   degreen - 1, myTurtle)
        sierpinski((getMid(
            points[0], points[2]), getMid(points[1], points[2]), points[2]),
                   degreen - 1, myTurtle)


# test
myTurtle = Turtle()
myWin = myTurtle.getscreen()
mypoints = ((-500, -250), (0, 500), (500, -250))
sierpinski(mypoints, 5, myTurtle)
myWin.exitonclick()