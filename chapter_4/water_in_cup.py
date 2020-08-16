'''
Author: star428
Date: 2020-08-14 18:24:47
LastEditTime: 2020-08-14 19:41:13
LastEditors: Please set LastEditors
Description: 解决桶装水问题,实际解决的为二进制序列，不停的向两个桶倒入水即可
FilePath: \Algorithms_and_Data_Strucures\chapter_4\water_in_cup.py
'''


def waterIn(bigBarrel, bigBarrel_water, smallBarrel, smallBarrel_water,
            requare_water):
    print("now full the big one")
    bigBarrel = bigBarrel_water
    print_barrel(bigBarrel, smallBarrel)

    bigBarrel, smallBarrel = waterRunIn(bigBarrel, smallBarrel,
                                        smallBarrel_water)  # from ,to
    print_barrel(bigBarrel, smallBarrel)

    if bigBarrel == requare_water:
        print("yes, the big one has the right water")
    else:
        print("now empty the small one")
        smallBarrel = 0
        print_barrel(bigBarrel, smallBarrel)
        bigBarrel, smallBarrel = waterRunIn(bigBarrel, smallBarrel,
                                            smallBarrel_water)
        print_barrel(bigBarrel, smallBarrel)
        waterIn(bigBarrel, bigBarrel_water, smallBarrel, smallBarrel_water,
                requare_water)


def waterRunIn(BarrelOne, BarrelTwo, BarrelTwo_water):
    print("now the water is from big to small")
    if BarrelOne > (BarrelTwo_water - BarrelTwo):
        BarrelOne -= (BarrelTwo_water - BarrelTwo)
        BarrelTwo = BarrelTwo_water
    else:
        BarrelTwo += BarrelOne
        BarrelOne = 0
    return BarrelOne, BarrelTwo


def print_barrel(bigBarrel, smallBarrel):
    print("now big has: " + str(bigBarrel) + " small has: " + str(smallBarrel))


# TEST
waterIn(0, 5, 0, 3, 2)
