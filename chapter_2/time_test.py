'''
Author: your name
Date: 2020-08-07 09:50:53
LastEditTime: 2020-08-07 10:32:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Algorithms_and_Data_Strucures\chapter_2\time_test.py
'''
import timeit
import random
# 索引时间为常数阶
list_index_time = timeit.Timer("a = list1[random.randint(0, n - 1)]",
                               "from __main__ import list1, random, n")
# 字典取值操作为常数阶
dict_get_value_time = timeit.Timer("b = dict1[random.randint(0, n - 1)]",
                                   "from __main__ import dict1, random, n")
n = 100000
list1 = list(range(n))
print(list_index_time.timeit(number=1000))

dict1 = {num: None for num in range(n)}
print(dict_get_value_time.timeit(number=1000))