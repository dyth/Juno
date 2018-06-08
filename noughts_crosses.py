#!/usr/bin/env python
"""player, winning and move conditions for noughts and crosses"""
import copy


# game information
initialBoard = [None, None, None, None, None, None, None, None, None]
players = [-1, 1]



def next_player(x):
    'return the identity of the next player'
    return players[(players.index(x) + 1) % 2]


def move(player, board, pos1, pos2):
    'board[3 * pos1 + pos2] = player'
    moved = copy.deepcopy(board)
    index = 3 * pos1 + pos2
    if (moved[index] == None):
        moved[index] = player
        return moved
    else:
        return None

    
def move_all(player, board):
    'return list of all possible next boards : a list list'
    if board == None:
        return
    moves = []
    for i in range(9):
        moved = copy.deepcopy(board)
        if (moved[i] == None):
            moved[i] = player
            moves.append(moved)
    return moves

    
def evaluate(board):
    'evaluate if there is a winner in the board'
    winner = [7, 56, 73, 84, 146, 273, 292, 448]
    for player in players:
        state = 0
        for i in range(9):
            state += (int(board[i] == player) << i)
        if state in winner:
            return player
        else:
            return 0
