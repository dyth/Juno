#!/usr/bin/env python
"""
train value_network using the TD(lambda) reinforcement algorithm
"""
from engine import *
from node import *
from play import *
from value_network import *
from noughts_crosses import *


def create_train_sequence(engines):
    'create a forest of nodes, their roots a new board position'
    board = initialBoard
    trace = []
    player = players[0]
    index = 0
    while evaluate(board) is None:
        node = engines[index].create_search_tree(board, player)
        trace.append(node)
        board = node.pv.board 
        player = next_player(player)
        index = int(not index)
    node = Node(board)
    node.reward = evaluate(board)
    trace.append(node)
    return trace


def TD_Lambda(engines, network):
    'return sequence of boards and reward for training'
    trace = create_train_sequence(engines)
    boards = [t.board for t in trace]
    reward = trace[-1].reward
    network.temporal_difference(boards, reward)
        

def train(engine, games):
    'train engine for self play in games'
    for _ in range(games):
        TD_Lambda([engine, engine], engine.policy)
    
    
if __name__ == "__main__":
    valueNetwork = ValueNet(0.01, 0.7)
    e = Engine(valueNetwork, 3)
    r = Engine(random, 1)
    #TD_Lambda([e, e], valueNetwork)
    for _ in range(1000):
        train(e, 20)
        win, lose, draw = 0, 0, 0
        for i in range(50):
            score = self_play([e, r])
            if score == 1:
                win += 1
            elif score == -1:
                lose += 1
            else:
                draw += 1
        print win, lose, draw, e.policy(initialBoard)

"""
e = Engine(optimal, 3)
r = Engine(random, 1)
win, lose, draw = 0, 0, 0
for i in range(50):
    score = self_play([e, r])
    if score == 1:
        win += 1
    elif score == -1:
        lose += 1
    else:
        draw += 1
win, lose, draw
"""
