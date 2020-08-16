'''
Author: star428
Date: 2020-08-14 09:33:30
LastEditTime: 2020-08-14 09:53:18
LastEditors: Please set LastEditors
Description: 汉诺塔递归实现
FilePath: \Algorithms_and_Data_Strucures\chapter_4\hanoyi.py
'''


def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(fromPole, toPole):
    toPole.insert(0, fromPole.pop(0))
    print(stack_a, stack_b, stack_c)


# test
stack_a = [1, 2, 3]
stack_b = []
stack_c = []
moveTower(len(stack_a), stack_a, stack_b, stack_c)
