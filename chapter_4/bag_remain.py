'''
Author: star428
Date: 2020-08-15 11:30:47
LastEditTime: 2020-08-15 15:51:19
LastEditors: Please set LastEditors
Description: 动态规划求解背包问题
FilePath: \Algorithms_and_Data_Strucures\chapter_4\bag_remain.py
'''


def bag(weight_value_List, bagWeight):
    mostValues = []  # 最多价值列表，下标是重量，内容是价值
    for weight in range(bagWeight + 1):
        values = 0  # 刚开始都是0
        for object in [ch for ch in weight_value_List if ch[0] <= weight]:
            if mostValues[weight - object[0]] + object[1] > values:
                values = mostValues[weight - object[0]] + object[1]
        mostValues.append(values)
    return mostValues[-1]


# test
weight_value_list = [(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)]
print(bag(weight_value_list, 12))
