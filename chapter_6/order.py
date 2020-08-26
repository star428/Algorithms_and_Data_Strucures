#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@contact: yewang863@gmail.com
@software: garner
@file: order.py
@time: 2020/8/24 下午2:41
@desc: 前序遍历，中序遍历与后序遍历
"""


def preOrder(tree):
    if tree:
        print(tree.getRootVal())
        preOrder(tree.getLeftChild())
        preOrder(tree.getRightChild())
