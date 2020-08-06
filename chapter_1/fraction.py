'''
Author: your name
Date: 2020-08-06 10:08:14
LastEditTime: 2020-08-06 10:32:41
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Algorithms_and_Data_Strucures\chapter_1\fraction.py
'''


class Fraction:
    def __init__(self, top, bottom) -> None:
        if int(top) != top or int(bottom) != bottom:
            raise ValueError("the top and the bottom must be int")
        if bottom < 0:
            top *= -1

        common = self.gcd(top, bottom)
        self.top = top // common
        self.bottom = bottom // common

    def gcd(self, m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = n
            n = oldm % oldn

        return n

    # 下面全是重写方法
    def __str__(self) -> str:  # 代码重写,自定义的str为输出对象的指针
        if abs(self.top) != abs(self.bottom) and self.top != 0:
            return str(self.top) + '/' + str(self.bottom)
        else:
            return str(int((self.top * self.bottom) / self.bottom))

    def __add__(self, otherfraction):
        new_top = self.top * otherfraction.bottom + \
                self.bottom * otherfraction.top
        new_bottom = self.bottom * otherfraction.bottom
       
        return Fraction(new_top, new_bottom)

    def __sub__(self, otherfraction):
        new_top = self.top * otherfraction.bottom - \
                self.bottom * otherfraction.top
        new_bottom = self.bottom * otherfraction.bottom
      
        return Fraction(new_top, new_bottom)

    def __eq__(self, otherfraction) -> bool:
        firsttop = self.top * otherfraction.bottom
        secondtop = otherfraction.top * self.bottom

        return firsttop == secondtop
