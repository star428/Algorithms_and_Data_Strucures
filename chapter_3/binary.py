'''
Author: star428
Date: 2020-08-08 10:06:34
LastEditTime: 2020-08-08 10:19:19
LastEditors: Please set LastEditors
Description: 十进制转换为二进制或任意进制
FilePath: \Algorithms_and_Data_Strucures\chapter_3\binary.py
'''
from stack import Stack


def decimal_to_binary(dec_number):
    stack = Stack()
    while dec_number > 0:
        rem = dec_number % 2
        stack.push(rem)
        dec_number = dec_number // 2

    string = ""
    while not stack.isEmpty():
        string = string + str(stack.pop())

    return int(string)


def baseConverter(dec_number, base):
    stack = Stack()
    digits = "0123456789ABCDEF"
    while dec_number > 0:
        rem = dec_number % base
        stack.push(rem)
        dec_number = dec_number // base

    string = ""
    while not stack.isEmpty():
        string = string + digits[stack.pop()]
    return string


# 测试
print(decimal_to_binary(10))
print(decimal_to_binary(1000))
print(baseConverter(1000, 16))
