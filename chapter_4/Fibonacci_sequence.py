'''
Author: star428
Date: 2020-08-14 15:17:18
LastEditTime: 2020-08-14 17:00:33
LastEditors: Please set LastEditors
Description: 递归实现斐波那契数列
FilePath: \Algorithms_and_Data_Strucures\chapter_4\Fibonacci_sequence.py
'''


def Fibonacci(num):
    if num == 1 or num == 2:
        return 1
    else:
        return Fibonacci(num - 1) + Fibonacci(num - 2)

# test
print(Fibonacci(10))