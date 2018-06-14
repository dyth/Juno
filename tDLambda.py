#!/usr/bin/env python
"""
train value_network using the TD(lambda) reinforcement algorithm
"""
from engine import *
from node import *
from play import *
from value_network import *
from noughts_crosses import *
import matplotlib.pyplot as plt


def create_train_sequence(engines):
    'create a forest of nodes, their roots a new board position'
    board = initialBoard
    
    r = Engine(random, 1, discount)
    board = r.minimax(board, players[0])
    
    trace = []
    player = players[1]
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


def TD_Lambda(engines, network, discount):
    'return sequence of boards and reward for training'
    trace = create_train_sequence(engines)
    boards = [t.board for t in trace]
    reward = trace[-1].reward
    network.temporal_difference(boards, reward, discount)
        

def train(engine, games):
    'train engine for self play in games'
    for _ in range(games):
        TD_Lambda([engine, engine], engine.policy, engine.discount)
    
    
if __name__ == "__main__":
    plt.ion()
    learningRate = 0.5
    discount = 0.7
    valueNetwork = ValueNet(learningRate, 0.7)
    e = Engine(valueNetwork, 3, discount)
    r = Engine(random, 1, discount)
    win, lose, draw = [], [], []
    testGamesNum = 10
    for _ in range(1000):
        # plot first before train
        w, l, d = 0, 0, 0
        for i in range(testGamesNum):
            score = self_play([e, r])
            if score == 1:
                w += 1
            elif score == -1:
                l += 1
            else:
                d += 1
            score = self_play([r, e])
            if score == -1:
                w += 1
            elif score == 1:
                l += 1
            else:
                d += 1
        w = float(w) / (2.0 * testGamesNum)
        l = float(l) / (2.0 * testGamesNum)
        d = float(d) / (2.0 * testGamesNum)
        print "Wins, Losses, Draws:", w, l, d, e.policy(initialBoard)
        win.append(w)
        lose.append(l)
        draw.append(d)
        plt.plot(win)
        plt.plot(lose)
        plt.plot(draw)
        plt.pause(0.001)
        plt.clf()

        # train
        train(e, 20)

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
