#!/usr/bin/env python
"""
train value_network using the TD-Leaf(lambda) reinforcement algorithm
"""
from tDLambda import *
from value_network import *


def get_leaf_pv(node):
    'get the leaf pv of a node'
    if node.pv is not None:
        return get_leaf_pv(node.pv)
    else:
        return node.board


def TD_Leaf(engines):
    'return sequence of boards and reward for training'
    trace = create_train_sequence(engines)
    boards = [get_leaf_pv(t) for t in trace]
    reward = trace[-1].reward
    return boards, reward


if __name__ == "__main__":
    e = Engine(optimal, 9)
    boards, reward = TD_Leaf([e, e])
    for b in boards:
        print b
    print reward
