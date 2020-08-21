'''
Author: star428
Date: 2020-08-17 10:02:20
LastEditTime: 2020-08-17 10:46:28
LastEditors: Please set LastEditors
Description: 哈希表的构成
FilePath: \Algorithms_and_Data_Strucures\chapter_5\hash_table.py
'''


class HashTable:
    def __init__(self) -> None:
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfaction(key, self.size)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                hashvalue = self.rehash(hashvalue, self.size)
                while self.slots[hashvalue] != None and\
                        self.slots[hashvalue] != key:
                    hashvalue = self.rehash(hashvalue, self.size)
                if self.slots[hashvalue] == None:
                    self.slots[hashvalue] = key
                    self.data[hashvalue] = data
                else:
                    self.data[hashvalue] = data

    def get(self, key):
        startslot = self.hashfaction(key, self.size)
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and\
                not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, self.size)
                if position == startslot:
                    stop = False
        return data

    def hashfaction(self, key, size):  # 简单的除余函数
        return key % size

    def rehash(self, oldhash, size):  # 加一除余
        return (oldhash + 1) % size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)
# test
hashtable = HashTable()
hashtable[54] = "cat"
hashtable[26] = "dog"
hashtable[93] = "lion"
hashtable[17] = "tiger"
hashtable[77] = "bird"
hashtable[31] = "cow"
hashtable[44] = "goat"
hashtable[55] = "pig"
hashtable[20] = "chicken"

print(hashtable[20])