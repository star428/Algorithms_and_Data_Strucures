'''
Author: star428
Date: 2020-08-12 14:45:22
LastEditTime: 2020-08-12 16:04:37
LastEditors: Please set LastEditors
Description: 递归实现进制转换
FilePath: \Algorithms_and_Data_Strucures\chapter_4\binary.py
'''


def toStr(n, base):
    converString = "0123456789ABCDEF"
    if n < base:
        return converString[n]
    else:
        return toStr(n // base, base) + converString[n % base]
