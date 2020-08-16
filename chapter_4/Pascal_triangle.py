'''
Author: star428
Date: 2020-08-15 10:54:28
LastEditTime: 2020-08-15 11:29:32
LastEditors: Please set LastEditors
Description: 帕斯卡尔三角形
FilePath: \Algorithms_and_Data_Strucures\chapter_4\Pascal_triangle.py
'''

triangle = []


def pascal(lines):
    for line in range(lines):
        temp = []
        for num in range(line + 1):
            temp.append(A_line_num(line, num))
        triangle.append(temp)


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def A_line_num(line, num): # 采用公式法
    return int(factorial(line) / (factorial(num) * factorial(line - num)))


