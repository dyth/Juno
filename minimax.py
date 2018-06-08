#!/usr/bin/env python
"""minimax to find optimal next move"""
from node import *

def minimax(n, i, player):
    'recursively interleave taking the maximum and then minimum values of \
    lists and sublists'
    # if there is no winner, do recursion downwards
    if n != None:
        if n.moves != []:
            moves = [minimax(m, (i+1)%2, next_player(player)) for m in n.moves]
            # Take the maximum or minimum depending on whether origin distance
            if i == 1:
                move = max(moves)
            elif i == 0:
                move = min(moves)
        # At nodes, if the player is the winner, then assign positive score.
        # Otherwise, assign negative score
        elif player == n.winner:
            move = 1
        elif next_player(player) == n.winner:
            move = -1
        elif None == n.winner and n.moves == []:
            move = 0
        return move


def decision(player, board):
    'input player ID and current state of board to generate the next state'
    root = fast_node(player, board)
    moves = [minimax(n, 0, next_player(player)) for n in root.moves]
    position = moves.index(max(moves))
    return move(player, board, position / 3, position % 3)
