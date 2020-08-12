'''
Author: star428
Date: 2020-08-08 09:02:10
LastEditTime: 2020-08-08 09:35:47
LastEditors: Please set LastEditors
Description: 解决简单多括号匹配问题
FilePath: \Algorithms_and_Data_Strucures\chapter_3\easy_bracket.py
'''
from stack import Stack


def parChacker(Simple_string):
    stack = Stack()
    balanced = True  # 解决右括号多于左括号问题
    index = 0

    while index < len(Simple_string) and balanced:
        if Simple_string[index] in '([{':
            stack.push(Simple_string[index])
            index += 1

        else:
            if stack.isEmpty():
                balanced = False
            else:
                top = stack.pop()
                if not match(top, Simple_string[index]):
                    balanced = False
                index += 1

    if balanced and stack.isEmpty():
        return True
    else:
        return False


def match(top, bottom):
    tops = "([{"
    bottoms = ")]}"
    if tops.index(top) == bottoms.index(bottom):
        return True
    else:
        return False


# 测试
string = "([{}])"
print(parChacker(string))