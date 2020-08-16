'''
Author: star428
Date: 2020-08-13 11:27:41
LastEditTime: 2020-08-13 11:29:57
LastEditors: Please set LastEditors
Description: 实现阶乘
FilePath: \Algorithms_and_Data_Strucures\chapter_4\factorial.py
'''


def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1

# test
print(factorial(4))