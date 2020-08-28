#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@contact: yewang863@gmail.com
@software: garner
@file: graphTest.py
@time: 2020/8/27 上午9:38
@desc:
"""
from graph import Graph

graph = Graph()
for index in range(6):
    graph.addVertex(index)

graph.addEdge(0, 1, 5)
graph.addEdge(0, 5, 2)
graph.addEdge(1, 2, 4)
graph.addEdge(2, 3, 9)
graph.addEdge(3, 4, 7)
graph.addEdge(3, 5, 3)
graph.addEdge(4, 0, 1)
graph.addEdge(5, 4, 8)
graph.addEdge(5, 2, 1)
