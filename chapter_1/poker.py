'''
Author: your name
Date: 2020-08-06 15:18:03
LastEditTime: 2020-08-06 18:56:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Algorithms_and_Data_Strucures\chapter_1\poker.py
'''


class Piece_Pocker:
    """描述一张扑克牌的类
    """
    def __init__(self):
        # 此时花色就是类型，包括大小王
        self.suit = None
        self.point = None

    def show_card(self):
        print(self.suit + ' *** *** ' + self.point)


class Pocker():
    """描述一副扑克牌的类，总共54张包括大小王

    Args:
        Piece_Pocker ([type]): [description]
    """
    def __init__(self):
        self.make_cards()

    def make_cards(self):
        # 每一张牌都是一个类，包括花色和点数
        self.cards = []
        suit = ['Spade', 'Heart', 'Diamond', 'Club']
        for suit_num in range(4):  # 有四个花色
            for numbers in range(1, 14):  # 数字从1到13
                card = Piece_Pocker()
                card.suit = suit[suit_num]
                if numbers == 11:
                    numbers = 'J'
                elif numbers == 12:
                    numbers = 'Q'
                elif numbers == 13:
                    numbers = 'K'
                elif numbers == 1:
                    numbers = 'A'
                else:
                    numbers = str(numbers)
                card.point = numbers
                self.cards.append(card)

        # 创立大小王,大小王无点数
        card_king = Piece_Pocker()
        card_king.suit = 'king'
        card_queen = Piece_Pocker()
        card_queen.suit = 'queen'
        self.cards.append(card_king)
        self.cards.append(card_queen)