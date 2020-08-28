#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@contact: yewang863@gmail.com
@software: garner
@file: Word_ladder.py
@time: 2020/8/27 上午10:14
@desc:
"""
from A_queue import Queue
from graph import Graph


def buildGraph(wordFile):
    d = {}
    graph = Graph()
    wfile = open(wordFile, 'r')

    for line in wfile:
        word = line[:-1]
        # 建立词桶
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i + 1:]
            if bucket in d.keys():
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # 构建边关系
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    graph.addEdge(word1, word2)


# 伪代码
def bfs(graph, start):  # start是一个Vertex
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)

    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == "white":
                nbr.setColor("gray")
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor("black")
