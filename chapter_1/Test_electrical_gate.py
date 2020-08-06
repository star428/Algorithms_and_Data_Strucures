'''
Author: your name
Date: 2020-08-05 15:37:59
LastEditTime: 2020-08-06 14:58:25
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Algorithms_and_Data_Strucures\chapter_1\Test_electrical_gate.py
'''
# import sys
# sys.path.append(
# "C:/Users/LEGION/Documents/GitHub/Algorithms_and_Data_Strucures/chapter_1")
# 虽然报错但是可以运行
from Electrical_network import Addgate, Orgate, NotGate, And_Not_Gate, Connector

gate1 = And_Not_Gate('G1')

print(gate1.getoutput())