'''
Author: star428
Date: 2020-08-10 10:25:11
LastEditTime: 2020-08-12 10:58:10
LastEditors: Please set LastEditors
Description: 回文数检测器
FilePath: \Algorithms_and_Data_Strucures\chapter_3\Palindrome_number.py
'''
from deque import Deque


def palChecker(aString):
    charDeque = Deque()

    for ch in aString:
        if ch != " ":
            charDeque.addRear(ch)

    stillEqual = True
    
    while charDeque.size() > 1:
        left_ch = charDeque.remove_rear()
        right_ch = charDeque.remove_front()
        if left_ch != right_ch:
            stillEqual = False
            break
            
    return stillEqual

# test
print(palChecker("a s  a")) 