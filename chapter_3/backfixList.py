'''
Author: star428
Date: 2020-08-09 08:41:48
LastEditTime: 2020-08-09 09:43:48
LastEditors: Please set LastEditors
Description: 后序表达式的计算
FilePath: \Algorithms_and_Data_Strucures\chapter_3\backfixList.py
'''
from stack import Stack
import string  # 内置类，使用方法


def postfixEval(postfixExpr):
    operandStack = Stack()  # 压数字的栈

    tokenList = postfixExpr.split()  # 执行的是string类的方法，实例化在编译阶段产生

    for token in tokenList:
        if token in "+-*/" and not operandStack.isEmpty():  # 是运算符就弹出两个数字运算
            right_operand = operandStack.pop()
            left_operand = operandStack.pop()
            result = domath(left_operand, right_operand, token)
            operandStack.push(result)
        else:  # 是数字就压入
            operandStack.push(token)
    result = operandStack.pop()
    if operandStack.isEmpty():
        return result
    else:
        return "error input"


def domath(left, right, token):
    left = int(left)
    right = int(right)

    if token == "+":
        return left + right
    elif token == "-":
        return left - right
    elif token == "*":
        return left * right
    elif token == "/":
        return left / right
    else:
        return 0


# test
print(postfixEval("+ 12 2 3 +"))