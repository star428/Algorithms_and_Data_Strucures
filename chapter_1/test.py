'''
Author: star428
Date: 2020-08-04 14:33:08
LastEditTime: 2020-08-06 10:08:24
LastEditors: Please set LastEditors
Description: 测试第一章所给出的源码
FilePath: \Algorithms_and_Data_Strucures\chapter_1\test.py
'''
print('hello', end='***')
print('world')
itemdict = {'item': 'banana', 'cost': 24}
print("The %(item)s costs %(cost).1f cents." % itemdict)
wordlists = ['cat', 'dog', 'rabbit']
for word in wordlists:
    for item in word:
        print(item)


def squareroot(num):
    root = num / 2
    for k in range(20):
        root = 0.5 * (root + (num / root))

    return root
