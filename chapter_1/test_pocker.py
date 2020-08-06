'''
Author: your name
Date: 2020-08-06 15:36:17
LastEditTime: 2020-08-06 18:56:20
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Algorithms_and_Data_Strucures\chapter_1\test_pocker.py
'''
from random import randint
from poker import Pocker


def remove_king_queen(pocker):
    """移除大小王

    Args:
        pocker ([type]): [description]
    """
    for card in pocker.cards[:]:
        if card.suit == 'king' or card.suit == 'queen':
            pocker.cards.remove(card)


def show_cards(cards):
    """展示牌库所有卡片

    Args:
        cards ([type]): [description]
    """
    for card in cards:
        card.show_card()


def count_points(cards):
    """计算点数

    Args:
        cards ([type]): [description]
    """
    for card in cards[:]:
        if card.point == 'A':
            cards.remove(card)
            cards.append(card)

    points = 0
    ten_points = ['10', 'J', 'Q', 'K']
    for card in cards:
        if card.point in ten_points:
            points += 10
        elif card.point == 'A':
            if points <= 9:
                points += 11
            else:
                points += 1
        else:
            points += int(card.point)

    return points


def check_win_lose(your_points, machines_points):
    """判断点数大小是否胜利

    Args:
        your_points ([type]): [description]
        machines_points ([type]): [description]
    """

    if your_points > machines_points:
        print("you win!")
        print("your points:" + str(your_points) + ' *** ' +
              "machines points:" + str(machines_points))
    else:
        print("you lose!")
        print("your points:" + str(your_points) + ' *** ' +
              "machines points:" + str(machines_points))


def run_game():
    pocker = Pocker()
    # 移除大小王
    remove_king_queen(pocker)

    your_cards = []
    your_points = 0
    machines_cards = []
    machines_points = randint(10, 20)
    print(machines_points)
    print("the game is the point of twenty one")
    while True:
        card = pocker.cards[randint(0, 52)]
        your_cards.append(card)

        print("your card now is:\n")
        show_cards(your_cards)

        your_points = count_points(your_cards)
        if your_points >= 21:
            print("you lose!")
            break

        choice = input("Do you want to get a card?[y/n]")
        if choice == 'y':
            continue
        else:
            check_win_lose(your_points, machines_points)
            break


run_game()