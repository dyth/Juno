#!/usr/bin/env python
"""play noughts and crosses against a random agent or human opposition"""
from engine import *
from value_network import *
from noughts_crosses import *


def self_play(engines):
    'engines is a list of engines and engines[0] moves first'
    board = initialBoard
    player = players[0]
    index = 0
    while evaluate(board) is None:
        board = engines[index].minimax(board, player)
        player = next_player(player)
        index = int(not index)
        pretty_print(board)
    return player


if __name__ == "__main__":
    e = Engine(optimal, 9)
    ran = Engine(random, 1)
    self_play([e, ran])
    #print e.minimax(initialBoard, players[0])
    #v = ValueNet()
    #e = Engine(v, 2)
    #pretty_print(e.minimax(initialBoard, players[0]))
    
