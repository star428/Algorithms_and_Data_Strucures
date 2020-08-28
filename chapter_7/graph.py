#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@contact: yewang863@gmail.com
@software: garner
@file: graph.py
@time: 2020/8/27 上午8:53
@desc:
"""


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectTo[nbr] = weight

    def __str__(self):
        return str(self.id) + " connect to : " + \
               str([x for x in self.connectTo.keys()])

    def getConnections(self):
        return self.connectTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList.keys():
            return self.vertList[n]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertList.keys()

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList.keys():
            nv = self.addVertex(f)
            self.numVertices += 1
        if t not in self.vertList.keys():
            nv = self.addVertex(f)
            self.numVertices += 1

        self.vertList[f].addNeighbor(t, cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
