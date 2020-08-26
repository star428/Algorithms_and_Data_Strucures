#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@contact: yewang863@gmail.com
@software: garner
@file: parsetree.py
@time: 2020/8/23 下午3:17
@desc:
"""
import sys

sys.path.append(
    '/home/star428/PycharmProjects/Algorithms_and_Data_Strucures/chapter_3')

from stack import Stack
from binarytree import BinaryTree
import operator


def buildParseTree(fpexp):  # 传入的为一个完全括号表达式
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i not in "+-*/)":
            currentTree.setRootVal(i)
            currentTree = pStack.pop()

        elif i in "+-*/":
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ")":
            currentTree = pStack.pop()

        else:
            raise ValueError("Unknown Operator: " + i)

    return eTree


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return int(parseTree.getRootVal())


def printExp(tree):
    if tree and tree.getLeftChild() and tree.getLeftChild():
        print("( ")
        printExp(tree.getLeftChild())
        print(tree.getRootVal())
        printExp(tree.getRightChild())
        print(" )")

    else:
        print(tree.getRootVal())

# test
line = "( 3 + ( 4 * 5 ) )"
tree = buildParseTree(line)
print(evaluate(tree))
printExp(tree)
