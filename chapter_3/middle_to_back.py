'''
Author: star428
Date: 2020-08-08 16:29:34
LastEditTime: 2020-08-08 16:59:11
LastEditors: Please set LastEditors
Description: 中序表达式转化为后序表达式的一般解法,时间复杂度n2左右
FilePath: \Algorithms_and_Data_Strucures\chapter_3\middle_to_back.py
'''
from stack import Stack
import string


def infixToPostfix(indixexpr):  # indixexpr是字符串
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opstack = Stack()  # 放入操作数和括号
    postfixList = []  # 最终显示的后续字符串
    tokenList = indixexpr.split()
    # 将字符串转换为列表(只有加入空格才能分开各个字符)

    for token in tokenList:
        if token in string.ascii_uppercase:
            postfixList.append(token)

        elif token == "(":  # 左括号直接压栈
            opstack.push(token)

        elif token == ")":
            # 右括号弹栈到最终postfixlist中直到遇到左括号（左括号也要弹）
            toptoken = opstack.pop()
            while toptoken != "(":
                postfixList.append(toptoken)
                toptoken = opstack.pop()

        else:
            # 剩下的就是一般运算符，在压栈前把比其优先级高的前几个全部弹出
            while (not opstack.isEmpty()) and \
                (prec[opstack.peek()] >= prec[token]):
                postfixList.append(opstack.pop())
            opstack.push(token)
    # 最后把栈全部清空（当然前面在括号匹配的情况下）
    while not opstack.isEmpty():
        postfixList.append(opstack.pop())

    return " ".join(postfixList)


# 测试
print(infixToPostfix("A + B + C"))