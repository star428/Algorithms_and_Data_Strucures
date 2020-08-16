'''
Author: star428
Date: 2020-08-12 16:42:38
LastEditTime: 2020-08-13 15:41:23
LastEditors: Please set LastEditors
Description: 绘制分形树
FilePath: \Algorithms_and_Data_Strucures\chapter_4\tree.py
'''
from turtle import Turtle
from random import randint


def tree(branchLen, branchwidth, turtle):
    angle = randint(15, 45)
    randomLen = randint(10, 15)
    if branchLen > 15:
        turtle.width(width=branchwidth)
        turtle.forward(branchLen)
        turtle.right(angle)
        tree(branchLen - randomLen, branchwidth - 1, turtle)
        turtle.left(angle * 2)  # 向左转抵消向右转的角度
        tree(branchLen - randomLen, branchwidth - 1, turtle)
        turtle.right(angle)  #回到原来准备回退
        turtle.backward(branchLen)  # 退回到初始点(针对最后一个末支而言)


turtle = Turtle()
myWins = turtle.getscreen()

turtle.left(90)
turtle.up()
turtle.backward(300)
turtle.down()
turtle.color("green")

tree(90, 9, turtle)
myWins.exitonclick()