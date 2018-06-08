#!/usr/bin/env python
"""generate a game tree of all possible moves from a rule file"""
from noughts_crosses import *


class value_node:
    'a node in a list tree'

    def __init__(self, player, board):
        'initialise new node with a board'
        
        # set conditions
        self.board = board
        self.player = player
        self.winner = evaluate(board)
        self.moves = []
        
        # if no winner and a move exist, swap the players and do all possible
        # moves
        if (self.winner == None) and (None in self.board):
            self.next = next_player(self.player)
            for m in move_all(self.next, self.board):
                # if no possible move, append None to list of moves
                if m != None:
                    self.moves.append(value_node(self.next, m))
                else:
                    self.moves.append(None)
                    
        # probability of player at index=player winning from current position
        self.pWins = [0.0 for _ in players]
        # if no winner, compute probability of winning for each player
        if self.winner == None:
            for p in players:
                self.cPWins = [m.pWins[int(p)] for m in self.moves if m != None]
                # if possible moves, normalise pWin
                if len(self.cPWins) != 0:
                    self.pWins[int(p)] = sum(self.cPWins) / len(self.cPWins)
        # if winner set pWin[winner] to be 1
        else:
            self.pWins[int(self.winner)] = 1.0


class fast_node:
    'a node in a list tree. Faster than the above because no probability'

    def __init__(self, player, board):
        'initialise new node with a board'
        
        # set conditions
        self.board = board
        self.player = player
        self.winner = evaluate(board)
        self.moves = []
        
        # if no winner and a move exist, swap the players and do all possible
        # moves
        if (self.winner == None) and (None in self.board):
            self.next = next_player(self.player)
            for m in move_all(self.next, self.board):
                # if no possible move, append None to list of moves
                if m != None:
                    self.moves.append(fast_node(self.next, m))
                else:
                    self.moves.append(None)
