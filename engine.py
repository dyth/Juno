#!/usr/bin/env python
"""
engine utilises a function policy to choose the best move using minimax
"""
from noughts_crosses import *


class Engine:

    def __init__(self, policy, searchDepth):
        # policy : fn board -> [-1.0, 1.0]'
        # searchDepth : int
        self.policy = policy
        self.searchDepth = searchDepth
        self.bestMove = None


    def minimax(self, board, player):
        'find self.bestMove using minimax to searchDepth'
        self.bestMove = None
        if player == players[0]:
            self.maximise(board, self.searchDepth, True)
        else:
            self.minimise(board, self.searchDepth, True)
        return self.bestMove
    
    
    def maximise(self, board, depth, rootNode):
        'maximise policy score for players[0]'
        if (depth == 0) or (evaluate(board) != None):
            return self.policy(board)
        moves = move_all(players[0], board)
        score = -2.0
        for m in moves:
            newScore = self.minimise(m, depth-1, False)
            if (newScore > score):
                score = newScore
                if rootNode:
                    self.bestMove = m
        return score
                
    
    def minimise(self, board, depth, rootNode):
        'minimise policy score for players[1]'
        if (depth == 0) or (evaluate(board) != None):
            return self.policy(board)
        moves = move_all(players[1], board)
        score = 2.0
        for m in moves:
            newScore = self.maximise(m, depth-1, False)
            if (newScore < score):
                score = newScore
                if rootNode:
                    self.bestMove = m
        return score


if __name__ == "__main__":
    e = Engine(optimal, 2)
    pretty_print(e.minimax(initialBoard, players[0]))
