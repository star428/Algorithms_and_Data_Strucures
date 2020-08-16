'''
Author: star428
Date: 2020-08-14 10:22:13
LastEditTime: 2020-08-14 15:11:28
LastEditors: Please set LastEditors
Description: 使用动态规划实现找零问题
FilePath: \Algorithms_and_Data_Strucures\chapter_4\get_change.py
'''


# 非动态规划的一般实现
def recMoneyChange(coinValueList, change, knowResults):
    minCoins = change
    if change in coinValueList:
        knowResults[change] = 1
        return 1
    elif knowResults[change] > 0:
        return knowResults[change]
    else:
        for i in [c for c in coinValueList if c < change]:  # 表示能用的而已
            numCoins = 1 + recMoneyChange(coinValueList, change - i,
                                          knowResults)  # 这里基本建立了树形结构
            if numCoins < minCoins:
                minCoins = numCoins
                knowResults[change] = minCoins
    return minCoins


# test
# print(recMoneyChange([1, 5, 10, 25], 63, [0] * 64))


# 动态规划实现
def dpMakeChange(coinValueList, change, minCoins, coinUsed):  # 从零开始的最小硬币数列表
    for cents in range(change + 1):  # 从零开始动态规划求解
        coinCounts = cents  # 默认为直接全部由1构成
        newCoin = 1
        for j in [ch for ch in coinValueList if ch <= cents]:
            if minCoins[cents - j] + 1 < coinCounts:  #前面求解的均为最小值此时带入即可
                coinCounts = minCoins[cents - j] + 1
                newCoin = j
        minCoins.append(coinCounts)
        coinUsed.append(newCoin)
    return minCoins[-1]


def print_coin(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin -= thisCoin


# test
coinUsed = []
print(dpMakeChange([1, 5, 10, 25], 21, [], coinUsed))
print_coin(coinUsed, 21)
